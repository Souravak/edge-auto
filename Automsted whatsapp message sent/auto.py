import pyautogui as pg
import time
import random

# pg.press("win")
# pg.write("c")
# pg.write("h")
# pg.write("r")
# pg.write("o")
# pg.write("m")
# pg.write("e")
# pg.press(" ")
# pg.write("j")
# pg.write("a")
# pg.write("d")
# pg.write("u")
# time.sleep(5)
# pg.press("enter")
# time.sleep(2)
# pg.write("https://web.whatsapp.com/")
# pg.press("enter")
# time.sleep(30)

# pg.press("tab", presses=8)
# pg.press("enter")
kich = "https://gpay.app.goo.gl/N3QmrE"
srv = "https://gpay.app.goo.gl/MTwytY"
Jerin = "https://gpay.app.goo.gl/HDy172"
Aparna = "https://gpay.app.goo.gl/jy6PxU6Px"
sreelakshmi = "https://gpay.app.goo.gl/4EQEs2"
msg="Help me get more floors and you could unlock a 9x floor booster " + srv + "\nHelp me get more floors and you could unlock a 9x floor booster " + kich
print(msg)
limit = 50
counter = 0

print("Program will run in 5 sec")
time.sleep(10)

remain = limit
for i in range(limit):
    n = random.randint(1, 10)
    print("Remaining msgs = ", i)
    for j in range(6):
        pg.write(msg)
        time.sleep(1)
        pg.press("Enter")
    pg.press("Tab", presses = 9)
    pg.press("down", presses = n)
    pg.press("Enter")
    
# kich : https://gpay.app.goo.gl/N3QmrE
# srv : https://gpay.app.goo.gl/MTwytY
# Jerin :  https://gpay.app.goo.gl/HDy172
# Aparna : https://gpay.app.goo.gl/jy6PxU6Px
# sreelakshmi : https://gpay.app.goo.gl/4EQEs2

