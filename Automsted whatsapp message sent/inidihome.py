import pyautogui as pg
import time
import random
print("Program will run in 5 sec")

x="https://gpay.app.goo.gl/HRDJ32"

time.sleep(5)
for i in range(100):
    n = random.randint(0,10)
    print("n = ", n)
    pg.write(x)
    time.sleep(5)
    pg.press("Enter")
    pg.press("Tab", presses=8)

    pg.press("down", presses = n)

    pg.press("Enter")

    # time.sleep(1)

# pyautogui.press(['left', 'left', 'left'])
# pyautogui.press('left', presses=3)
# with pyautogui.hold('shift'):
#         pyautogui.press(['left', 'left', 'left'])