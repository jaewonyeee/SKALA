# -------------------------------------------------------------
# 작성자 : 
# 작성목적 : KDT 교육용 고급 자료구조 (Deque, Stack, Queue 활용)
# 작성일 : 2025-02-20
# 본 파일은 KDT 교육을 위한 Sample 코드이므로 작성자에게 모든 저작권이 있습니다.
# 
# 변경사항 내역 (날짜, 변경목적, 변경내용 순으로 기입)
# 
# -------------------------------------------------------------

from collections import deque

def browser_navigation(commands):
    history = deque()  # 방문한 사이트를 저장하는 스택
    back_stack = deque()  # 뒤로 가기 기능을 위한 보조 스택
    current_page = None

    for command in commands:
        if command == "back":
            if history:
                back_stack.append(current_page)  # 현재 페이지를 back_stack에 저장
                current_page = history.pop()  # history에서 가장 최근 페이지로 이동
        else:
            if current_page:
                history.append(current_page)  # 현재 페이지를 history에 저장
            current_page = command  # 새 페이지 방문
            back_stack.clear()  # 새로운 방문이 있으면 뒤로 가기 기록 초기화

    return current_page, list(history)  # 현재 페이지와 방문 기록 반환

# 테스트 코드
commands = ["google.com", "facebook.com", "back", "twitter.com", "back"]
print(browser_navigation(commands))