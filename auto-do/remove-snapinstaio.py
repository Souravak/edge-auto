import pyautogui as pg
import time

time.sleep(5)
for i in range(1):
    pg.press("down")
    pg.press("f2")
    pg.press("left")
    pg.press("delete",presses=15)
    pg.press("enter")
