import pyautogui
# 스크린 샷 찍기
# img = pyautogui.screenshot()
# img.save("screenshot.png") # 파일로 저장

# pyautogui.mouseInfo()
# 1797,52 219,88,96 #DB5860


# pixel = pyautogui.pixel(1797, 52)
# print(pixel)

pixel = pyautogui.pixel(1797, 52)
print(pyautogui.pixelMatchesColor(28, 18, (219,88,96)))
print(pyautogui.pixelMatchesColor(28, 18, pixel))
print(pyautogui.pixelMatchesColor(28, 18, (219,88,97)))