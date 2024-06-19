import pyautogui, webbrowser
from time import sleep 

numero = 545722584

webbrowser.open("https://web.whatsapp.com/send?phone="+numero)

sleep(5)

for i in range(24):
    pyautogui.typewrite("Me muero")
    pyautogui.press("enter")