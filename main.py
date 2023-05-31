import pyautogui
import time
import random

def click_center():
    screen_width, screen_height = pyautogui.size()
    center_x = screen_width // 2
    center_y = screen_height // 2
    pyautogui.click(center_x, center_y)

while True:
    click_center()
    interval = 30 + random.randint(-10, 10)  # Интервал в секундах с рандомным смещением
    time.sleep(interval)  # 30 секунд + interval
