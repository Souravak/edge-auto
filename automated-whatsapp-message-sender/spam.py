import pyautogui as pg
import time
import random
msg = "Ni poda kaaperkki kazhuveri kallanayeente nayinte mone"

limit = 232
counter = 0
print("Program will run in 5 sec")
time.sleep(5)
remain = limit
for i in range(limit):
    n = random.randint(1, 10)
    remain-=1
    print("Remaining msgs = ", remain)
    counter+=1
    pg.write(msg)
    # time.sleep(0.5)
    pg.press("Enter")