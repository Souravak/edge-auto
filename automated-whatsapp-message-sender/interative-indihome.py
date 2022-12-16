import pyautogui as pg
import time
import random
print("Enter Message to send : ", end = "") 
msg = input()
print("Enter the number of times to send the msg : ", end = "")
limit = int(input()) 
print("Program will run in 5 sec")
time.sleep(5)
remain = limit
for i in range(limit):
    n = random.randint(1, 10)
    remain-=1
    print("Remaining msgs = ", remain)
    pg.write(msg)
    time.sleep(5)
    pg.press("Enter")
    pg.press("Tab", presses = 8)
    pg.press("down", presses = n)
    pg.press("Enter")