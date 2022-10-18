import win32api, win32con
import time
import keyboard
from PIL import Image, ImageGrab
from pynput.mouse import Button, Controller

col = [(0, 208, 1)]
x, y = 500, 150
mouse = Controller()
time.sleep(8)
num = 2
image = ImageGrab.grab()
color = image.getpixel((x, y))
while True:
    color = image.getpixel((x, y))
    if color == (0, 208, 0):
        tx, ty = x - 940, y - 560
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, tx, ty, 0, 0)
        time.sleep(0.003)
        mouse.click(Button.left)
        time.sleep(0.003)
        txx, tyx= tx * (-1), ty * (-1)
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, txx, tyx, 0, 0)
        time.sleep(0.003)
        image = ImageGrab.grab()
        x = 500
    if keyboard.is_pressed('q'):
        print('you stopped the program')
        break
    if x > 1400:
        num += 1
        if num % 2 == 0:
            x = 513
        elif num % 2 == 0:
            x = 556
        else:
            x = 587
        image = ImageGrab.grab()
    y += 100
    if y > 950:
        x += 30
        y = 150


