import pyautogui as pg
import time 
print("PC will hibernate in 10 sec")
time.sleep(10)
pg.keyDown("win")
pg.press("x")
pg.keyUp("win")
pg.press("u")
pg.press("r")
