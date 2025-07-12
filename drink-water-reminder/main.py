#Pync for macOS
#Plyer for cross-platform

import time   
from pync import Notifier

while True:
    print("Please sip some water!")  
    Notifier.notify("It is important to stay hydrated.", title="Drink Water Reminder")  
    time.sleep(60*60)


#plyer will on windows, linux, macOS
#Pync will only work on macOS


# import time   
# from plyer import notification

# while True:
#     print("Please sip some water!")  
#     notification.notify(title="Please drink some water", 
#                         message = "You need to drink some water",
#                         app_icon = None,  # You can specify an icon path if you have one)
#                         timeout = 10)  # Notification will stay for 10 seconds
    
#     time.sleep(60*60)