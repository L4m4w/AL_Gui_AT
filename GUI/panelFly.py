import pyautogui
import time
import os


#  Фокусируемся на приложении;
os.startfile(r"D:\ASTRA\Debian 10.x 64-bit.vmx")


def Navigator():

    #  Наводим курсор на объект "Стартовая панель-меню" и нажимаем на него;
    pyautogui.click(x=984, y=908, button='left')

    panel_check = pyautogui.locateOnScreen('panelFly.png')

    if panel_check == None:
        pass

    #  Ожидаем, мало ли система будет долго открывать меню;
    time.sleep(2)

    pyautogui.click(x=984, y=908, button='left')

    finish_check = pyautogui.locateOnScreen('homeScreen.png')

    if finish_check != None:
        print('Test panelFly = Ok!')


Navigator()
