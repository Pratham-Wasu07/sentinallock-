from services.lock_service import lock_windows

print("Locking PC in 3 seconds...")

import time
time.sleep(3)

lock_windows()