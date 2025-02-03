while True:
    user_input = input("문장을 입력하세요 (종료하려면 '!quit' 입력): ")
    if user_input.lower() == '!quit':
        print("프로그램을 종료합니다.")
        break
    print("입력한 문장:", user_input)
