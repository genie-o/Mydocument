# 튜플의 unpacking
tup = ("피카츄", 20, "Seoul")
name, age, city = tup
print(name)
print(age)
print(city)

# 기존에 값변경 하던 방법 (tmp 필요했다)
a = 10
b    = 20

tmp = a
a = b
b = tmp

# 파이썬에서 값 변경
a,b = 10, 20
a,b = b,a

# 튜플 결합하기
t1 = (1,2,3)
t2 = ('a', 'b', 'c')
t3 = t1 + t2
print(t3)

# 튜플 요소 할당하기 : *
t2 = t1 * 3
print(t2)

# in 연산자
tub = (1,2,'a','b')
print('a' in tup)

tupList = [("피카츄",100), ("꼬북이", 70), ("파이리", 45)]
for i, j in tupList:
    print("%s님의 점수는 %d점 입니다." %(i, j))

# 인덱싱, 슬라이싱
tup = ("global", [1,2,3], [4,5,6])
print(tup[1][1])
print(tup[1][1:])
print(tup[2][:2])

