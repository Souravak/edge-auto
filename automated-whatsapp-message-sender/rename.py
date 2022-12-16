import pyautogui as pg
import time
import random


print("Program will run in 5 sec")
time.sleep(10)

limit = 19
for i in range(limit):
    pg.press("right")
    pg.press("f2")
    pg.press("right")
    pg.write("apk")
    pg.press("enter",presses=2)
print("Finished")
