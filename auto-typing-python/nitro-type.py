import pyautogui as pg
import time
time.sleep(3)
text = "The quick brown fox jumps over the lazy dog."
for i in range(len(text)):
    pg.write(text[i])