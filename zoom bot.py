import subprocess
import pyautogui
import time
from datetime import datetime


def signIn(meeting_id,password):
    #Open's Zoom Application from the specified location
    subprocess.Popen("C:\\Users\\Pc\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")
    time.sleep(3)

    #Click's join button
    joinbtn=pyautogui.locateCenterOnScreen("joinbtn.png")
    pyautogui.moveTo(joinbtn)
    pyautogui.click()
    time.sleep(1)

    #Type the meeting id
    meetingidbtn=pyautogui.locateCenterOnScreen("meetingidbtn.png")
    pyautogui.moveTo(meetingidbtn)
    pyautogui.write(meeting_id)
    time.sleep(2)

    #To turn of video and audio
    mediaBtn=pyautogui.locateAllOnScreen("btn.png")
    for btn in mediaBtn:
        pyautogui.moveTo(btn)
        pyautogui.click()
        time.sleep(1)

    #To join
    join=pyautogui.locateCenterOnScreen("join.png")
    pyautogui.moveTo(join)
    pyautogui.click()
    time.sleep(2)

    #Enter's passcode to join meeting

    passcode=pyautogui.locateCenterOnScreen("passcode.png")
    pyautogui.moveTo(passcode)
    pyautogui.write(password)
    time.sleep(1)

    #Click's on join button
    joinmeeting=pyautogui.locateCenterOnScreen("joinmeeting.png")
    pyautogui.moveTo(joinmeeting)
    pyautogui.click()
    time.sleep(1)
while True:
    #To get current time
    now = datetime.now().strftime("%H:%M")
    meeting_time= "02:26"
    if now==meeting_time:
        meeting_id = "whatever the meeting id is"
        password = "password"
        time.sleep(5)
        signIn(meeting_id, password)
        time.sleep(2)
        print('signed in')
        break
