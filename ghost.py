import pyautogui

#location = pyautogui.locateOnScreen('down.png')
#print(location)
#point = pyautogui.center(location)
pyautogui.moveTo() # move mouse to the window 
pyautogui.dragTo() # focus the window 
#pyautogui.click() # simulate left click 
#pyautogui.typewrite() # type something 

status = pyautogui.click('down.png')
print(status)
status = pyautogui.click('down.png')
print(status)
