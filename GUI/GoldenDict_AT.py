import pyautogui
import time
import os


#  Фокусируемся на приложении;
os.startfile(r"D:\ASTRA\Debian 10.x 64-bit.vmx")


def Navigator():

    #  Наводим курсор на объект "Стартовая панель-меню" и нажимаем на него;
    pyautogui.click(x=984, y=908, button='left', clicks=2)

    #  Ожидаем, мало ли система будет долго открывать меню;
    time.sleep(2)

    print(pyautogui.position())

    #  Наводим курсор на объект "Офис" и нажимаем на него;
    pyautogui.click(x=998, y=398, button='left')

    time.sleep(2)

    print(pyautogui.position())

    #  Наводим курсор на приложение "GoldenDict" и нажимаем на него;
    pyautogui.click(x=998, y=398, button='left')

    time.sleep(3)

    finish_check = pyautogui.locateOnScreen('GoldenDict.png')

    if finish_check != None:
        print('Test GoldenDict = Ok!')


Navigator()
