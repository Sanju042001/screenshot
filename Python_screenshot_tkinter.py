import pyautogui
from tkinter import *
import time

k=Tk()
k.title("Python Screenshot")
k.geometry("250x120")
def Screenshot():
    s=Sec.get()
    s=int(s)
    time.sleep(s)
    pyautogui.screenshot("Macha1.png")
    n=Label(k, text="Screenshot have been taken")
    n.pack()

    
E=Label(k, text="Enter the time in second")
Sec=Entry(k,width=10)
b=Button(k, text="Take screenshot", width=20, command=Screenshot)
E.pack()
Sec.pack()
b.pack()
k.mainloop()
'''    
sec=int(input("Enter the delay"))
time.sleep(sec)
pyautogui.screenshot()
name=pyautogui.screenshot("Screenshot1.png")
'''
