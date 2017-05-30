import pyautogui  # pyautogui

##### 키 입력 (자동차 제어) #######################
def keyInput(centerStatus):

    try:
        if centerStatus < -12:
            pyautogui.keyDown("right")
            pyautogui.keyUp("right")

        elif centerStatus > 12:
            pyautogui.keyDown("left")
            pyautogui.keyUp("left")

    except:
        pass

    pass
