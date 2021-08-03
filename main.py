from plyer import notification
import psutil
import time

already_notified = False

while True:
    current_apps = (p.name() for p in psutil.process_iter())

    if "Zoom.exe" in current_apps:
        if not already_notified:
            notification.notify( 
                title = "Reminder:",
                message = "Remember to check if your mic is muted and camera turned off",
                timeout = 30
            )
            already_notified = True

    else:
        already_notified = False       
        
    time.sleep(5)