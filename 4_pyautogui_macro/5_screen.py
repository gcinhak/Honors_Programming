import pyautogui as pag

# 1. 스크린 샷 찍어서 파일로 저장
# img = pag.screenshot()
# img.save("screenshot.png") # 파일로 저장

# 2. 특정 위치를 픽셀 값 확인
# pag.mouseInfo()
# pixel = pag.pixel(1874, 59) # (237, 162, 0)
# print(pixel)

# 3. pixelMatchesColor 컬리값 비교
pixel = pag.pixel(1874, 59)
print(pag.pixelMatchesColor(1874, 59, (237, 162, 0)))
print(pag.pixelMatchesColor(1874, 59, pixel))
print(pag.pixelMatchesColor(1874, 59, (237, 162, 1)))