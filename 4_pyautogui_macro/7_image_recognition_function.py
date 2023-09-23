import pyautogui as pag

# 자동화 대상이 바로 보여지지 않는 경우
# 1. 프로그램이 시작 할 때, 자동화 대상이 없으면 종료
# notepad_add_icon = pag.locateOnScreen("notepad_add_icon.png")
# if notepad_add_icon:
#     pag.click(notepad_add_icon)
# else:
#     print("발견 실패")

# 2. 찾을 때 까지 계속 대기
# while notepad_add_icon is None:
#     notepad_add_icon = pag.locateOnScreen("notepad_add_icon.png")
#     print("발견 실패")
# pag.click(notepad_add_icon)

# 3. 일정 시간동안 기다리기 (TimeOut)
# import time
# import sys

# timeout = 5 # 5초 대기
# start = time.time() # 시작 시간 설정
# notepad_add_icon = None
# while notepad_add_icon is None:
#     notepad_add_icon = pag.locateOnScreen("notepad_add_icon.png")
#     end = time.time() # 종료 시간 설정
#     if end - start > timeout: # 지정한 10초를 초과하면
#         print("시간 종료")
#         sys.exit()

# def find_target(img_file, timeout=5):
#     start = time.time()
#     target = None
#     while target is None:
#         target = pag.locateOnScreen(img_file)
#         end = time.time()
#         if end - start > timeout:
#             break
#     return target
#
# def click_target(img_file, timeout=5):
#     target = find_target(img_file, timeout)
#     if target:
#         pag.click(target)
#     else:
#         print("[Timeout {}s] Target not found ({})."\
#               .format(timeout, img_file))
#         sys.exit()
#
# pag.click(notepad_add_icon)
#
# click_target("notepad_add_icon.png", 3)


