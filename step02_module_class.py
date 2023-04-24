'''
모듈 클래스
 - 파이썬에서 제공하는 클래스
 - 유형
   1) builtins 모듈 클래스 : 내장 클래스 
   2) import 모듈 클래스 : 가져오기 클래스 
'''

# 1. builtins 모듈 클래스 
import builtins
dir(builtins)

# 1) 자료구조 관련 
lst = list(range(10))
t = tuple(lst)
s = set(lst)
d = dict({'name' : 'hong', 'age' : 30})

type(lst)
type(d)

# 2) 자료형 변환
int(32.5)
float(10)
bool(10)
str(10) + '대'
 


# 2. import 클래스
from datetime import date # 날짜 객체 생성 클래스 
import datetime 

today = date(2023, 2, 22) # 클래스명() : 생성자  & 멤버변수 초기화 
print(today)
print(type(today))

# 객체 멤버 : 필드(속성) + 메소드 
dir(today)

# 객체.필드 : 값 
today.year # 2023
# 객체.메소드()
today.weekday() # 2

























