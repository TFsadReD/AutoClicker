from pyautogui import click
from time import sleep
from keyboard import is_pressed

positions = [(1349, 995), (1812, 995)]
delay = 0.1
running = False
i = 0

ver = "Release 1.0"
print(f"AutoClicker {ver}\nНажми F8 чтобы ЗАПУСТИТЬ/ОСТАНОВИТЬ кликер, ESC чтобы выйти")

while True:
    if is_pressed("esc"):
        print(">>> Выход из программы...")
        break

    if is_pressed("F8"):
        running = not running
        print(">>> Кликер ВКЛЮЧЕН" if running else ">>> Кликер ВЫКЛЮЧЕН")
        while is_pressed("F8"):
            sleep(0.1)

    if running:
        x, y = positions[i % len(positions)]
        click(x, y)
        print(f">>> Клик {i+1} по координатам: {x}, {y}")
        i += 1
        sleep(delay)
    else:
        sleep(0.1)
