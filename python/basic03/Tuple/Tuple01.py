'''
군집자료형 : str, list, tuple, dict, set
*** 튜플 Tuple ***
리스트 : []
튜플 : (,)
튜플은 요소의 값을 수정할 수가 없다. immutable
데이터가 한개일때는 쉼표 반드시 기술
데이터가 여러개일때는, 소괄호 생략 가능 (쉼표로 구분)

'''

# 빈 튜플
t1 = ()
print(t1)
print(type(t1))

# 한개의 요소만 대입할경우
t2 = ("abc",)
print(t1)
print(type(t1))

# 요소가 두 개 이상일 경우
t3 = 1,2,3
print(t3)
print(type(t3))

t4 = (1,2,"a",True)
print(t4)
print(t4[0])
#t4[0] = 10
#print(t4)

t5 = (1,2,[3,4,5],6,7)
print(t5)
t5[2][0] = 100
print(t5)
t5[2][0] = "def"
print(t5)
