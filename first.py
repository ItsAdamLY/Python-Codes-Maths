import keyboard as kb
from time import *

while True:
    kb.press('h')
    sleep(2)
    kb.press('w')
    sleep(2)
    kb.release('w')
    kb.press('s')
    sleep(2)
    kb.release('s')