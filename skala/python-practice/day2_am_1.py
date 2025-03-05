# -------------------------------------------------------------
# 작성자 : 
# 작성목적 : KDT 교육용 데코레이터 실습 목적 코드
# 작성일 : 2025-02-20
# 본 파일은 KDT 교육을 위한 Sample 코드이므로 작성자에게 모든 저작권이 있습니다.
# 
# 변경사항 내역 (날짜, 변경목적, 변경내용 순으로 기입)
# 
# -------------------------------------------------------------

import time
import logging
import functools

# 로그 설정
logging.basicConfig(filename="execution_log.txt", level=logging.INFO, format="%(asctime)s - %(message)s")

def log_time(func):
    """ 함수의 실행 시간을 측정하고 로그로 저장하는 데코레이터 """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()  # 시작 시간 기록
        result = func(*args, **kwargs)  # 원래 함수 실행
        end_time = time.time()  # 종료 시간 기록
        elapsed_time = end_time - start_time  # 실행 시간 계산

        log_message = f"Function '{func.__name__}' executed in {elapsed_time:.4f} seconds"
        logging.info(log_message)  # 로그 파일에 기록
        print(log_message)  # 콘솔 출력

        return result

    return wrapper

# 테스트용 함수
@log_time
def example_function():
    """ 간단한 테스트 함수 (2초 대기) """
    time.sleep(2)
    print("작업 완료!")

# 실행
example_function()
