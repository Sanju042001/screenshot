import pyautogui
import time
sec=int(input("Enter the delay"))
time.sleep(sec)
pyautogui.screenshot()
name=pyautogui.screenshot("Screenshot1.png")