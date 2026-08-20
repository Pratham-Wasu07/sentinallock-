# sentinallock-
# FaceLock

### AI-Powered Continuous Desktop Security System

FaceLock is an AI-powered desktop security system that uses **face recognition and liveness detection** for continuous user authentication. It detects unauthorized users and spoofing attempts, automatically locks the system, and logs suspicious activity for enhanced security.

---

## What Makes FaceLock Different?...

Unlike basic face-unlock systems that only verify your identity during login, FaceLock is designed for **continuous security monitoring**.

It can:

* Continuously verify the authorized user
* Detect basic spoofing attempts such as photos or replay attacks
* Detect unknown users
* Automatically lock the system when the user leaves
* Record suspicious access attempts
* Maintain authentication and security logs
* Process sensitive face data locally

---

## How It Works

```text
                ┌─────────────┐
                │   Webcam    │
                └──────┬──────┘
                       ↓
                ┌─────────────┐
                │Face Detection│
                └──────┬──────┘
                       ↓
                ┌─────────────┐
                │   Liveness  │
                │   Detection │
                └──────┬──────┘
                       ↓
                ┌─────────────┐
                │     Face    │
                │ Recognition  │
                └──────┬──────┘
                       ↓
              ┌──────────────────┐
              │ Authorized User? │
              └────────┬─────────┘
                       ↓
                ┌──────┴──────┐
                ↓             ↓
             YES              NO
                ↓             ↓
        Continue Access    Security Event
                ↓             ↓
        Continuous Check   Log / Capture
                ↓             ↓
        User Leaves?       Lock System
                ↓
             LOCK
```

---

## Key Features

### Continuous Authentication

FaceLock periodically verifies that the authorized user is still present instead of checking the identity only once.

### Liveness Detection

The system analyzes whether the detected face belongs to a real person, helping protect against basic photo and replay attacks.

### Intruder Detection

When an unknown person is detected, FaceLock can:

* Record the failed attempt
* Capture an image
* Create a security event
* Lock the system after repeated attempts

### Automatic Locking

If the authorized user leaves the camera's view for a configured period, FaceLock can automatically lock the workstation.

### Security Logging

Authentication events can include:

```text
Time
User
Authentication Status
Confidence Score
Liveness Result
Security Event
```

### Privacy-Focused

Face recognition can be performed locally, reducing the need to send sensitive biometric information to external servers.

---

## Technology Stack

| Technology             | Purpose                        |
| ---------------------- | ------------------------------ |
| Python                 | Core application               |
| OpenCV                 | Computer vision and camera     |
| Face Recognition Model | Identity verification          |
| Liveness Model         | Anti-spoofing                  |
| PySide6                | Desktop interface              |
| SQLite                 | Local event storage            |
| NumPy                  | Image and numerical processing |

---

## Project Structure

```text
FaceLock/
│
├── core/
│   ├── camera.py
│   ├── detector.py
│   ├── recognizer.py
│   ├── liveness.py
│   ├── security.py
│   └── locker.py
│
├── ui/
│   ├── dashboard.py
│   ├── enrollment.py
│   └── settings.py
│
├── models/
│   ├── recognition/
│   └── anti_spoof/
│
├── database/
│   └── facelock.db
│
├── assets/
├── logs/
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Example Security Status

```text
╔══════════════════════════════════╗
║          FACELOCK SECURITY       ║
╠══════════════════════════════════╣
║ System Status     : SECURE       ║
║ Camera            : ACTIVE       ║
║ User              : AUTHORIZED   ║
║ Face Confidence   : 96%          ║
║ Liveness          : PASS         ║
║ Monitoring        : ACTIVE       ║
╚══════════════════════════════════╝
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/FaceLock.git
cd FaceLock
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run FaceLock

```bash
python app.py
```

---

## User Enrollment

The enrollment process captures multiple face samples to improve recognition across different angles and lighting conditions.

```text
Start Enrollment
       ↓
Capture Face Samples
       ↓
Generate Face Embeddings
       ↓
Store Locally
       ↓
User Enrolled
```

---

## Roadmap

### Authentication

* [x] Face detection
* [x] Face recognition
* [ ] Continuous authentication
* [ ] Multi-user support

### Security

* [ ] Advanced liveness detection
* [ ] Photo attack detection
* [ ] Replay attack detection
* [ ] Intruder snapshots
* [ ] Automatic workstation locking
* [ ] Failed-attempt protection

### Dashboard

* [ ] Real-time security status
* [ ] Authentication history
* [ ] Security event timeline
* [ ] Confidence monitoring
* [ ] Configurable security settings

### Deployment

* [ ] Windows startup integration
* [ ] Standalone `.exe`
* [ ] Background monitoring
* [ ] Performance optimization

---

## Privacy & Security

FaceLock is intended primarily as an educational and personal security project.

Never commit sensitive biometric information to GitHub.

Do not upload:

```text
.env files
Passwords
API keys
Real face images
Biometric databases
Private logs
Personal information
```

---

## Disclaimer

FaceLock is an additional security layer and should not be considered a replacement for operating-system security mechanisms such as passwords, PINs, encryption, or hardware-backed authentication.

Face recognition can produce false positives and false negatives, so appropriate security thresholds and fallback authentication should be used.

---

## Contributing

Contributions and improvements are welcome.

You can contribute by:

* Reporting bugs
* Improving face recognition
* Improving liveness detection
* Optimizing performance
* Improving the UI
* Adding security features
---

## Author

**Pratham Wasu**

Computer Science Engineering Student

`AI` • `Cybersecurity` • `Computer Vision` • `Software Development`

---


