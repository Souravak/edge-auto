import pyautogui as pg
import time
print("Program will run in 5 sec")
time.sleep(5)
for i in range(100):
    x=str(i+1)+'.Hello World!'
    pg.write(x)
    time.sleep(0.1)
    pg.press("Enter")