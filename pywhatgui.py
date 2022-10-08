import pyautogui
import time
user = input("Enter Msg You want To type: ")
todo = int(input("Enter No. of time you want to type: "))
time.sleep(5)
cout = 0
print("starting")
def send():#
    tot=0
    cout = 0
    while cout != todo:
        pyautogui.typewrite(user)
        pyautogui.press('enter')
        cout = cout + 1
        
send()
print("complete")

