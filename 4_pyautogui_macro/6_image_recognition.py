import pyautogui as pag

# 1. 화면 상에 같은 이미지 찾아서 클릭
# file_icon = pag.locateOnScreen("file_icon.png")
# print(file_icon)
# pag.click(file_icon)

# 2. 화면 상에 같은 이미지 찾아서 마우스 커서 이동
# option_icon = pag.locateOnScreen("option_icon.png")
# pag.moveTo(option_icon)

# 3. 화면 상에 같은 이미지 없으면 None 리턴
# screen = pag.locateOnScreen("screenshot.png")
# print(screen)

# 4. 같은 이미지 모두 찾아서 클릭
for pos in pag.locateAllOnScreen("checkbox.png"):  # print(pos)
    pag.click(pos)

# 5. 같은 이미지가 여러개라도 처음 만나는 하나만 클릭하고 종료됨.
# checkbox = pag.locateOnScreen("checkbox.png")
# pag.click(checkbox)

# 6. 같은 이미지가 오른쪽 밑에 있으면 찾는데 시간이 오래 걸림
# option_icon = pag.locateOnScreen("option_icon.png")
# pag.moveTo(option_icon)

# 속도 개선
# 1. GrayScale
# option_icon = pag.locateOnScreen("option_icon.png", grayscale=True)
# pag.moveTo(option_icon)

# 2. 범위 지정
# option_icon = pag.locateOnScreen("option_icon.png", region=(1794, 891, 1904-1794, 929-891))
# pag.moveTo(option_icon)

# 3. 정확도 조정
# pip install openve-python
# run_btn = pag.locateOnScreen("run_btn.png", confidence=0.9) # 90%
# pag.moveTo(run_btn)

