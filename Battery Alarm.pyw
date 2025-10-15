import psutil
import winsound
import time
from threading import Thread
from PIL import Image, ImageDraw
import pystray

# Thresholds
LOW_BATTERY = 40
HIGH_BATTERY = 97
CHECK_INTERVAL = 2  # seconds

# Beep settings
BEEP_FREQUENCY = 2000  # Hz
BEEP_DURATION = 1000   # milliseconds
BEEP_GAP = 1        # seconds between beeps

# State variables
alert_active = False
stop_alert = False

# Function to beep continuously
def beep_loop():
    while not stop_alert:
        winsound.Beep(BEEP_FREQUENCY, BEEP_DURATION)
        time.sleep(BEEP_GAP)

# Create a simple icon for the tray
def create_image():
    width = 64
    height = 64
    image = Image.new('RGBA', (width, height), (0, 0, 0, 0))  # Transparent background
    dc = ImageDraw.Draw(image)
    
    # Draw battery body (rounded rectangle)
    dc.rounded_rectangle([12, 20, 52, 44], radius=3, fill=(34, 34, 34), outline=(255, 255, 255), width=2)
    
    # Draw battery terminal (small rectangle on right)
    dc.rectangle([52, 28, 56, 36], fill=(255, 255, 255))
    
    # Draw battery fill (green bar inside)
    dc.rectangle([16, 24, 44, 40], fill=(76, 175, 80))

    return image

# Function for tray icon
def setup_tray():
    def quit_action(icon, item):
        global stop_alert
        stop_alert = True
        icon.stop()

    icon = pystray.Icon("BatteryAlert", create_image(), "Battery Alert",
                        menu=pystray.Menu(pystray.MenuItem("Quit", quit_action)))
    icon.run()

# Start tray icon in a separate thread
Thread(target=setup_tray, daemon=True).start()

# Main monitoring loop
while True:
    battery = psutil.sensors_battery()
    if battery is None:
        time.sleep(CHECK_INTERVAL)
        continue

    percent = battery.percent
    charging = battery.power_plugged

    if percent <= LOW_BATTERY and not charging:
        if not alert_active:
            alert_active = True
            stop_alert = False
            Thread(target=beep_loop, daemon=True).start()
    elif percent >= HIGH_BATTERY and charging:
        if not alert_active:
            alert_active = True
            stop_alert = False
            Thread(target=beep_loop, daemon=True).start()
    else:
        # Battery status safe → stop alert if active
        if alert_active:
            stop_alert = True
            alert_active = False

    time.sleep(CHECK_INTERVAL)
