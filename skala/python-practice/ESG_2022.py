# -------------------------------------------------------------
# 작성자 : 
# 작성목적 : KDT 교육용 Python pandas, numpy, seaborn, sklearn 실습 목적 코드
# 작성일 : 2025-02-08

# 본 파일은 KDT 교육을 위한 Sample 코드이므로 작성자에게 모든 저작권이 있습니다.
# 
# 변경사항 내역 (날짜, 변경목적, 변경내용 순으로 기입)
# 
# -------------------------------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


# 파일 경로 설정
file_path = 'ESG_2022.csv'  # 파일 경로를 현재 디렉토리로 변경

# 데이터 로드 (UTF-8 인코딩 시도 후 실패 시 CP949 시도)
try:
    df = pd.read_csv(file_path, encoding='utf-8')
except UnicodeDecodeError:
    try:
        df = pd.read_csv(file_path, encoding='cp949')
    except UnicodeDecodeError:
        df = pd.read_csv(file_path, encoding='euc-kr')  # 다른 인코딩 시도


# 컬럼 이름 확인
print("컬럼 이름 확인:")
print(df.columns)
print("컬럼 이름 확인 완료")

# 데이터프레임 정보 확인
print("\n데이터프레임 정보:")
print(df.info())

print("\n처음 5행:")
print(df.head())

# '컬럼 찾기
year_column = [col for col in df.columns if 'year' in col or 'year' in col.lower()]
total_emission_column = [col for col in df.columns if 'Total Emissions' in col or 'total emissions' in col.lower()]
net_emission_column = [col for col in df.columns if 'Net Emissions' in col or 'net emissions' in col.lower()]
energy_column = [col for col in df.columns if 'Energy' in col or 'energy' in col.lower()]
fuel_combustion_column = [col for col in df.columns if 'fuel combustion' in col or 'Fuel Combustion' in col.lower()]


if not year_column or not total_emission_column:
    raise KeyError("데이터에 '연도' 또는 '순배출량' 관련 컬럼이 없습니다. 파일을 확인하세요.")

#year_column = year_column[0]
#emission_column = emission_column[0]

year_column = year_column[0]
total_emission_column = total_emission_column[0]
net_emission_column = net_emission_column[0]
energy_column = energy_column[0]
fuel_combustion_column = fuel_combustion_column[0]

# 결측치 처리
df[total_emission_column] = pd.to_numeric(df[total_emission_column], errors='coerce')  # 숫자형 변환
df.fillna({total_emission_column: 0}, inplace=True)

# 연도별 순배출량 합계 계산
yearly_emission = df.groupby(year_column)[total_emission_column].sum()
print("\n연도별 순배출량 합계:")
print(yearly_emission)

# 예측 모델 학습
X = yearly_emission.index.values.reshape(-1, 1)
y = yearly_emission.values
model = LinearRegression()
model.fit(X, y)

# 향후 5년 예측
future_years = np.arange(yearly_emission.index.max() + 1, yearly_emission.index.max() + 6)
future_X = future_years.reshape(-1, 1)
future_predictions = model.predict(future_X)

print("\n향후 5년 예측:")
print(future_predictions)


# 연도별 순배출량 합계 계산
yearly_emission = df.groupby(year_column)[total_emission_column].sum()
print("\n연도별 순배출량 합계:")
print(yearly_emission)

# 시각화: 연도별 순배출량 꺾은선 그래프
plt.figure(figsize=(10, 6))
plt.plot(yearly_emission.index, yearly_emission.values, marker='o', label='Net Emissions')
plt.title('CO2 Net Emissions by Year')
plt.xlabel('Year')
plt.ylabel('CO2 Emissions (Net)')

# x축 범위 설정
plt.xlim(yearly_emission.index.min(), yearly_emission.index.max())

# x축 눈금 설정 (5년 단위로 표시)
plt.xticks(range(yearly_emission.index.min(), yearly_emission.index.max()+1, 5))

# 격자 추가
plt.grid(True)

# 범례 추가
plt.legend()

# 그래프 이미지 파일로 저장
image_file_path = 'esg_prediction.png'  # 저장할 이미지 파일 경로 및 이름 설정
plt.savefig(image_file_path)  # 그래프를 이미지 파일로 저장
print(f"\n그래프가 '{image_file_path}'로 저장되었습니다.")

# 그래프 출력
plt.show()

