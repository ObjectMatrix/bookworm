import pyautogui
import time

pyautogui.FAILSAFE = False

while True:
  time.sleep(300)
  for m in range(0, 100):
    pyautogui.moveTo(0, m * 2)
  for p in range(0, 3):
    pyautogui.press('shift')

