from utils.resource_path import resource_path
import sys
from PySide6.QtWidgets import QApplication
from ui.dashboard import Dashboard

app = QApplication(sys.argv)

with open(resource_path("assets/style.qss")) as f:
    app.setStyleSheet(f.read())

window = Dashboard()
window.show()

sys.exit(app.exec())