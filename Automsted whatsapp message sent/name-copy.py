import pyautogui as pg
import time
import random


print("Program will run in 5 sec")
time.sleep(10)

limit = 134
for i in range(limit):
    pg.keyDown("alt")
    pg.press("tab")
    pg.keyUp("alt")
    pg.press("down")
    pg.press("f2")
    pg.keyDown("ctrl")
    pg.press("c")
    pg.keyUp("ctrl")
    time.sleep(1)
    pg.keyDown("alt")
    pg.press("tab")
    pg.keyUp("alt")
    pg.keyDown("ctrl")
    pg.press("v")
    pg.keyUp("ctrl")
    pg.press("enter")

print("Finished")
