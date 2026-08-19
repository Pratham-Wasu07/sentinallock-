import asyncio
from datetime import datetime

import cv2
from PySide6.QtCore import QTimer
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import (
    QApplication,
    QFrame,
    QHBoxLayout,
    QLabel,
    QListWidget,
    QMainWindow,
    QVBoxLayout,
    QWidget,
)

from camera.camera_service import CameraService
from services.bluetooth_service import BluetoothService
from services.lock_service import lock_windows

class Dashboard(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("🛡 SentinelLock")
        self.resize(1350, 800)

        self.camera = CameraService()
        self.bluetooth = BluetoothService()

        self.user_present = False
        self.phone_nearby = False
        self.absent_seconds = 0
        self.lock_delay = 10

        self.previous_person = "No Face"
        self.current_person = "No Face"

        self.imageLabel = QLabel()
        self.imageLabel.setFixedSize(850, 550)
        self.imageLabel.setStyleSheet(
            "background:black;border:2px solid #555;border-radius:10px;"
        )

        self.userStatus = QLabel("❌ No Owner")
        self.phoneStatus = QLabel("📱 Phone : Not Connected")
        self.lockStatus = QLabel("🔒 Laptop : Safe")
        self.countdownStatus = QLabel("⏳ Countdown : --")

        for lbl in (
            self.userStatus,
            self.phoneStatus,
            self.lockStatus,
            self.countdownStatus,
        ):
            lbl.setStyleSheet("font-size:18px;padding:8px;")

        panel = QFrame()
        panel.setStyleSheet("QFrame{border:2px solid gray;border-radius:10px;}")

        layout = QVBoxLayout()
        title = QLabel("Security Status")
        title.setStyleSheet("font-size:22px;font-weight:bold;")
        layout.addWidget(title)
        layout.addWidget(self.userStatus)
        layout.addWidget(self.phoneStatus)
        layout.addWidget(self.lockStatus)
        layout.addWidget(self.countdownStatus)
        layout.addStretch()
        panel.setLayout(layout)

        self.logList = QListWidget()
        self.add_log("🛡 SentinelLock Started")

        top = QHBoxLayout()
        top.addWidget(self.imageLabel,3)
        top.addWidget(panel,1)

        root = QVBoxLayout()
        head = QLabel("🛡 SentinelLock")
        head.setStyleSheet("font-size:30px;font-weight:bold;")
        root.addWidget(head)
        root.addLayout(top)
        root.addWidget(QLabel("📋 Security Logs"))
        root.addWidget(self.logList)

        container = QWidget()
        container.setLayout(root)
        self.setCentralWidget(container)

        self.camera_timer = QTimer(self)
        self.camera_timer.timeout.connect(self.update_frame)
        self.camera_timer.start(30)

        self.countdown_timer = QTimer(self)
        self.countdown_timer.timeout.connect(self.update_countdown)
        self.countdown_timer.start(1000)

        self.bluetooth_timer = QTimer(self)
        self.bluetooth_timer.timeout.connect(self.check_phone)
        self.bluetooth_timer.start(5000)

    def check_phone(self):
        try:
            self.phone_nearby = asyncio.run(self.bluetooth.phone_nearby())
            if self.phone_nearby:
                self.phoneStatus.setText("📱 Phone : Connected")
            else:
                self.phoneStatus.setText("📱 Phone : Not Connected")
        except Exception as e:
            print("Bluetooth Error:", e)

    def update_frame(self):
        data = self.camera.get_frame()

        if data is None:
            return

        frame, owner_present, person = data
        print("Frame:", type(frame))
        print("Person:", person)

        if frame is None:
            return

        self.user_present = owner_present
        self.current_person = person

        if person != self.previous_person:
            if person.lower() == "pratham":
                self.add_log("✅ Owner Recognized")
            elif person == "Unknown":
                self.add_log("🚨 Unknown Person Detected")
            else:
                self.add_log("👋 Owner Left")
            self.previous_person = person

        if person.lower() == "pratham":
            self.userStatus.setText("🟢 Owner : Pratham")
            self.lockStatus.setText("🔓 Laptop : Safe")
            self.countdownStatus.setText("⏳ Countdown : --")
        elif person == "Unknown":
            self.userStatus.setText("🚨 Unknown Person")
        else:
            self.userStatus.setText("❌ No Owner")
        if frame is None:
            print("Frame is None")
            return

        print(frame.shape)
        
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = frame.shape
        image = QImage(frame.data, w, h, ch * w, QImage.Format_RGB888)
        self.imageLabel.setPixmap(QPixmap.fromImage(image))

    def update_countdown(self):
        if self.user_present or self.phone_nearby:
            self.absent_seconds = 0
            return

        self.absent_seconds += 1
        remaining = self.lock_delay - self.absent_seconds

        if remaining > 0:
            self.countdownStatus.setText(f"⏳ Countdown : {remaining} sec")

        if self.absent_seconds == 1:
            self.add_log("⏳ Countdown Started")

        if self.absent_seconds >= self.lock_delay:
            self.lockStatus.setText("🔒 Laptop Locked")
            self.add_log("🔒 Laptop Locked")
            lock_windows()
            self.absent_seconds = 0

    def add_log(self, message):
        ts = datetime.now().strftime("%H:%M:%S")
        self.logList.insertItem(0, f"[{ts}] {message}")
        while self.logList.count() > 100:
            self.logList.takeItem(100)

    def closeEvent(self, event):
        self.camera.release()
        event.accept()

if __name__ == "__main__":
    app = QApplication([])
    window = Dashboard()
    window.show()
    app.exec()