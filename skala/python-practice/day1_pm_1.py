# -------------------------------------------------------------
# 작성자 : 
# 작성목적 : KDT 교육용 Python pandas, numpy, seaborn, sklearn 실습 목적 코드
# 작성일 : 2025-02-08
# 본 파일은 KDT 교육을 위한 Sample 코드이므로 작성자에게 모든 저작권이 있습니다.
# 
# 변경사항 내역 (날짜, 변경목적, 변경내용 순으로 기입)
# 
# -------------------------------------------------------------
import csv
from statistics import mean
students = [
    {"name": "Alice", "scores": {"math": 85, "science": 90, "english": 88}},
    {"name": "Bob", "scores": {"math": 78, "science": 85, "english": 92}},
    {"name": "Charlie", "scores": {"math": 92, "science": 88, "english": 95}},
    {"name": "David", "scores": {"math": 76, "science": 82, "english": 79}},
    {"name": "Eve", "scores": {"math": 89, "science": 94, "english": 87}}
]


# 1. 각 과목별 평균 점수 계산
def calculate_subject_averages(students):
    subjects = students[0]['scores'].keys()
    averages = {}
    for subject in subjects:
        scores = [student['scores'][subject] for student in students]
        averages[subject] = mean(scores)
    return averages
subject_averages = calculate_subject_averages(students)
print("1. 과목별 평균 점수:", subject_averages)

# 2. 평균 점수가 가장 높은/낮은 과목 찾기
best_subject = max(subject_averages, key=subject_averages.get)
worst_subject = min(subject_averages, key=subject_averages.get)
print(f"2. 평균 점수가 가장 높은 과목: {best_subject}, 가장 낮은 과목: {worst_subject}")

# 3. 학생별 평균 점수 계산 및 최고/최저 학생 찾기
def calculate_student_averages(students):
    return {student['name']: mean(student['scores'].values()) for student in students}
student_averages = calculate_student_averages(students)
best_student = max(student_averages, key=student_averages.get)
worst_student = min(student_averages, key=student_averages.get)
print(f"3. 평균 점수가 가장 높은 학생: {best_student}, 가장 낮은 학생: {worst_student}")

# 4. 90점 이상인 과목이 하나라도 있는 학생들
high_scorers = [student['name'] for student in students if any(score >= 90 for score in student['scores'].values())]
print("4. 90점 이상인 과목이 있는 학생들:", high_scorers)

# 5. 모든 과목에서 80점 이상을 받은 학생들
consistent_scorers = [student['name'] for student in students if all(score >= 80 for score in student['scores'].values())]
print("5. 모든 과목에서 80점 이상인 학생들:", consistent_scorers)

# 6. CSV 파일로 저장
with open('student_scores.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Math', 'Science', 'English'])
    for student in students:
        writer.writerow([student['name']] + list(student['scores'].values()))
print("6. 학생 성적 데이터를 CSV 파일로 저장했습니다.")

# 7. CSV 파일 읽기 및 각 과목별 최고 점수 학생 찾기
def find_top_scorers(filename):
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        data = list(reader)
    top_scorers = {}
    for subject in ['Math', 'Science', 'English']:
        top_scorer = max(data, key=lambda x: int(x[subject]))
        top_scorers[subject] = top_scorer['Name']
    return top_scorers
top_scorers = find_top_scorers('student_scores.csv')
print("7. 각 과목별 최고 점수 학생:")

for subject, name in top_scorers.items():
    print(f"   {subject}: {name}")
