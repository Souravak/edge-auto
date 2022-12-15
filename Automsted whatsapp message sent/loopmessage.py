import pyautogui as pg
import time
print("Program will run in 5 sec")
time.sleep(5)
for i in range(1000):
    # x=str(i+1)+'Alooo'
    x='https://gpay.app.goo.gl/nfsznb'
    pg.write(x)
    time.sleep(1)
    pg.press("Enter")