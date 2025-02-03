import re

def is_valid_password(password):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    return bool(re.match(pattern, password))

while True:
    password = input("비밀번호를 입력하세요 (종료하려면 '!quit' 입력): ")
    if password.lower() == '!quit':
        print("프로그램을 종료합니다.")
        break
    
    if is_valid_password(password):
        print("유효한 비밀번호입니다.")
    else:
        print("비밀번호가 조건을 충족하지 않습니다. (최소 8자, 대문자, 소문자, 숫자, 특수문자 포함)")
