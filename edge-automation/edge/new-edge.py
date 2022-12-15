import pyautogui as pg
import time
from random_word import RandomWords
random_words = RandomWords()
limit = 10

for i in range(limit):
    print("Search ",i+1, end="")
    pg.keyDown("ctrl")
    pg.press("t")
    pg.keyUp("ctrl")
    pg.write(random_words.get_random_word())
    pg.press("Enter")
    time.sleep(2)
    print(" - Done")

#auto close after 30 seconds
time.sleep(30)
pg.keyDown("ctrl")
for i in range(limit): pg.press("w")
pg.keyUp("ctrl")
pg.write("https://rewards.bing.com/pointsbreakdown")
pg.press("Enter")
print("Search Completed Successfully")