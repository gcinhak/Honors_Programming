import pyautogui as pag

# 무한 루프 탈출 방법
# 1. 마우스 커서를 모서리로 이동
# 2. Ctrl + Alt + del

while True:
    pag.moveTo(100,500,duration=0.2)
    pag.moveTo(1000,500,duration=0.2)