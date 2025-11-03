import time
import os

alarm_time = input("Enter alarm time (HH:MM:SS): ")
print(f"Setting alarm for {alarm_time}...")

while True:
    current_time = time.strftime("%H:%M:%S")
    if current_time == alarm_time:
        print("Wake up! It's time!")
        for i in range(5):
            os.system('echo -n "\a"')  # makes a beep sound in terminal
        break
    time.sleep(1)
