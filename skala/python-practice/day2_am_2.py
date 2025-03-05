# -------------------------------------------------------------
# 작성자 : 
# 작성목적 : KDT 교육용 선형 자료 구조 실습 목적 코드
# 작성일 : 2025-02-20
# 본 파일은 KDT 교육을 위한 Sample 코드이므로 작성자에게 모든 저작권이 있습니다.
# 
# 변경사항 내역 (날짜, 변경목적, 변경내용 순으로 기입)
# 
# -------------------------------------------------------------

import time
import numpy as np

# 리스트와 NumPy 배열 생성
size = 1_000_000
py_list = list(range(size))
numpy_array = np.arange(size)

# Python 리스트 성능 측정
start_time = time.time()
py_list_squared = [x**2 for x in py_list]
end_time = time.time()
print(f"Python 리스트 실행 시간: {end_time - start_time:.4f} 초")

# NumPy 배열 성능 측정
start_time = time.time()
numpy_array_squared = numpy_array ** 2
end_time = time.time()
print(f"NumPy 배열 실행 시간: {end_time - start_time:.4f} 초")