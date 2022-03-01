import pyautogui, keyboard, time
print('кнопка: "X"(латиница), закончить: "Z"')
coords = []
colors = {}
while not keyboard.is_pressed("Z"):
    time.sleep(0.1)
    if keyboard.is_pressed("X"):
        coords.append(pyautogui.position())
        print(coords[-1])
        pyautogui.moveRel(200, 0, duration=0.1)
        colors[coords[-1]] = pyautogui.pixel(*coords[-1])
        pyautogui.moveRel(-200, 0, duration=0.1)
    if keyboard.is_pressed("Z"):
        break
    
print("Приступаю к выполнению!")
for i in coords:
    time.sleep(3)
    if colors[i] != (255, 255, 255):
        pyautogui.moveTo(i[0], i[1], 1)
        print('Было ваше - стало нашe')
    else:
        pyautogui.moveTo(i[0], i[1], 3)
    pyautogui.click()

pyautogui.alert (text = 'Готово', title = 'Бот', button = 'Спасибки')

