from pyautogui import click
from time import sleep
from keyboard import add_hotkey, wait

positions = [(1349, 995), (1812, 995)]
delay = 0.1
running = False

def clicker():
    global running
    i = 0
    while True:
        if running:
            x, y = positions[i % len(positions)]
            click(x, y)
            print(f"Клик {i+1} по координатам: {x}, {y}")
            i += 1
            sleep(delay)
        else:
            sleep(0.1)

print("Нажми F8 чтобы ЗАПУСТИТЬ/ОСТАНОВИТЬ кликер, ESC чтобы выйти.")

add_hotkey("F8", lambda: globals().__setitem__("running", not running))

wait("esc")
