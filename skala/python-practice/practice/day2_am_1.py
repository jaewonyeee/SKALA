#0------------ 
# 
# 
# 


"""데이터 분석에 필요한 라이브러리"""
import numpy
import pandas as pd
import matplotlib.pyplot as plt

"""데이터 로드 및 데이터 정보확인"""
df = pd.read_csv('ESG_CO2_2021.csv')
#df.info()
#print(df.head())
#print(df.describe())

"""결측치 여부 확인"""
# print(df.isnull())

"""데이터 타입 확인 및 변환"""
# print(df.dtypes)

# df['net emission'] = df['net emission'].astype(int) #정수형으로 변환
# print(df.head()) 

# print(df.dtypes)

"""데이터 다루기"""
print(df.min())
print(df.max())

"""데이터 시각화"""
c