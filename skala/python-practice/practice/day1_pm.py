# --------------------------------------------------------------------------
# 작성자 : 이재원
# 작성목적 : Python 데이터 분석 기초 실습 목적 코드
# 작성일 : 2025-03-04
# 본 파일은 작성자에게 모든 저작권이 있습니다.
# --------------------------------------------------------------------------
"""moudle for csv file reading and writing"""

import csv

students = [
    {"name": "Alice", "scores": {"math": 85, "science": 90, "english": 88}},
    {"name": "Bob", "scores": {"math": 78, "science": 85, "english": 92}},
    {"name": "Charlie", "scores": {"math": 92, "science": 88, "english": 95}},
    {"name": "David", "scores": {"math": 76, "science": 82, "english": 79}},
    {"name": "Eve", "scores": {"math": 89, "science": 94, "english": 87}}
]


def calculate_student_averages(people):
    """function for calculating student average"""
    people_averages = {}

    for person in people:
        total_score = sum(person['scores'].values())  # 모든 과목 점수 합산
        average_score = total_score / len(person['scores'])  # 과목 수로 나누어 평균 계산
        people_averages[person["name"]] = average_score  # 학생 이름을 key로 평균 저장

    return people_averages

# 학생별 평균 점수 계산
student_averages = calculate_student_averages(students)

# 최고 & 최저 평균 점수 찾기
MAX_STUDENT = None
MIN_STUDENT = None
max_score = float('-inf')  # 아주 작은 값으로 초기화
min_score = float('inf')   # 아주 큰 값으로 초기화

for student, avg in student_averages.items():
    if avg > max_score:  # 최고 점수 갱신
        max_score = avg
        MAX_STUDENT = student

    if avg < min_score:  # 최저 점수 갱신
        min_score = avg
        MIN_STUDENT = student

# 결과 출력
print("학생별 평균 점수:", student_averages)
print(f"가장 평균 점수가 높은 학생: {MAX_STUDENT} ({max_score:.2f})")
print(f"가장 평균 점수가 낮은 학생: {MIN_STUDENT} ({min_score:.2f})")

# 90점 이상인 과목이 하나라도 있는 학생들
high_scorers = [student['name'] for student in students
if any(score >= 90 for score in student['scores'].values())]
print("90점 이상인 과목이 있는 학생들:", high_scorers)

# 모든 과목에서 80점 이상을 받은 학생들
standard_scorers = [student['name'] for student in students
if all(score >= 80 for score in student['scores'].values())]
print("모든 과목에서 80점 이상인 학생들:", standard_scorers)

# CSV 파일로 저장
with open('student_scores.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Math', 'Science', 'English'])
    for student in students:
        writer.writerow([student['name']] + list(student['scores'].values()))
print("학생 성적 데이터를 CSV 파일로 저장했습니다.")


def find_top_scorers(filename):
    """function for reading csv file & finding top scorers"""
    with open(filename, 'r', encoding="utf-8") as cfile:
        reader = csv.DictReader(cfile)  # CSV 파일을 딕셔너리 형태로 읽기
        data = list(reader)  # 데이터를 리스트로 변환

    top_scorers_dict = {}  # 최고 점수 학생을 저장할 딕셔너리

    for subject in ['Math', 'Science', 'English']:
        top_student = None  # 최고 점수 학생 초기화
        top_score = float('-inf')  # 최소값으로 초기화

        for student in data:
            score = int(student[subject])  # 현재 학생의 점수 가져오기
            if score > top_score:  # 현재 점수가 최고 점수보다 크다면 업데이트
                top_score = score
                top_student = student['Name']

        top_scorers_dict[subject] = top_student  # 최고 점수 학생 저장

    return top_scorers_dict

# CSV 파일에서 각 과목별 최고 점수 학생 찾기
top_scorers = find_top_scorers('student_scores.csv')

# 결과 출력
print("각 과목별 최고 점수 학생:")
for subject, name in top_scorers.items():
    print(f"{subject}: {name}")
