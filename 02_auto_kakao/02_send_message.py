import pandas as pd
import pyautogui
import pyperclip
import time

# 모든 키 출력
# print(pyautogui.KEYBOARD_KEYS)

# 카카오 검색창 위치 이동
# x, y = pyautogui.position()
# print(f'x:{x}, y:{y}')

# 엑셀파일 불러오기
df = pd.read_excel('./today_report.xlsx')

# 이름, 메세지 변수명 df 입력

# nm = df['이름'][0]
# print(f'{nm}')
# # print(df['메시지'][0])
# msg = df['메시지'][0]

def find_nm_send_message(df):
    # print(df['이름'][0])
        # 카카오 검색으로 이름 찾기
        # 클립보드에 텍스트 복사
    for i, row in df.iterrows():
        # 검색버튼 클릭
        pyautogui.moveTo(1753, 203, duration=0.1)
        pyautogui.click()  # 왼쪽마우스 클릭
        time.sleep(2)
        # 변수명 설정
        nm = row['이름']
        msg = row['메시지']
        # 이름 복사
        pyperclip.copy(f'{nm}')
        # 붙여넣기
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(2)

        # 이름창 클릭
        pyautogui.moveTo(1585, 374, duration=0.1)
        # 더블클릭
        pyautogui.click(clicks=2)
        pyautogui.doubleClick()
        time.sleep(2)

        # 채팅창 이동
        pyautogui.moveTo(1375, 865, duration=0.1)
        pyautogui.click()#왼쪽마우스 클릭
        time.sleep(2)

        # 검색한 이름으로 메세지 보내기
        # 클립보드에 텍스트 복사
        pyperclip.copy(f'{msg}')
        # 붙여넣기
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(2)

        # 전송버튼 클릭
        pyautogui.moveTo(1524, 970, duration=0.1)
        pyautogui.click()#왼쪽마우스 클릭

        # 스크린샷 찍기
        pyautogui.screenshot(f'screenshot_test_{i}.png', region=(1161,508,400,500))#스크린샷 마우스 위치X,Y, 스크린샷 크기X,Y

        # 채팅창 닫기버튼클릭
        pyautogui.moveTo(1567, 127, duration=0.1)
        pyautogui.click()#왼쪽마우스 클릭
        time.sleep(2)

        # 검색버튼 닫기 클릭
        pyautogui.moveTo(1796, 279, duration=0.1)
        pyautogui.click()  # 왼쪽마우스 클릭
        time.sleep(2)

# 엑셀 파일을 파라미터로 넣기
find_nm_send_message(df)