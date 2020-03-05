'''
*** 연산자 operator ***
산술연산자 : + - * / %
대입연산자 : =
복합대입연산자 : += -= *= /= %=
비교 연산자 : > >= < <= ++ !=
논리 연산자 : = True / False
멤버 연산자 : in / not in
식별 연산자 : is / is not
'''

# 대입 연산자
x = 10
y = 10
z = 10
x=y=z=10
print(x)
print(y)
print(z)

x,y,z = 10,20,30
print(x)
print(y)
print(z)


'''
# 문제1. 분자, 분모를 하나씩 입력받고, 몫과 나머지를 출력하세요
son = int(input("분자:"))
mom = int(input("분모:"))

print("몫은 %d 이다" % (son//mom))
print("나머지 %d 이다" % (son%mom))


# 문제2. 1000초를 몇분 몇초로 나누어 출력하세요
print("%d분 %d초" % (1000//60, 1000%60))
'''


print("=======")
# 복합대입 연산지
num1 = 10
num2 = 20

num1 = num1 + 10
num1 -= 10
print(num1)

# 비교연산자 : 결과 True/False
print(num1 != num2)

# 논리 연산자 : and or not
'''
a and b : a(비교연산식)와 b 둘 다 참이어야 참
a or b : a 와 b 가 모두 거짓이어야 거짓, 둘중 하나라도 참이면 참
not a : a가 거짓이어야 참
'''

print("=======")
# 비교연산자를 조정해서 출력문 전체 true 결과가 나오게 변경해보세요
a,b,c,d = 10,9,8,7
print(a > b and c > d)
print(a <= b or c > d)
print(not(a == b or c < d))


print("=======")
# 문제1. 복합대입 연산자를 이용해서 연결
a = "Python"
b = "is fun!!!"
c = "Java"
d = "is not fun!!!"

a+=b
c+=d
a+=c
print(a)


# 문제1. 화폐매수 구하기
'''
금액을 입력받고 최소 화폐 매수를 구해서 출력하세요.
예) 67800원 입력받았을 경우 출력
'''

money = int(input("금액입력:"))
print("5만원 : %d장" % (money//50000))
print("1만원 : %d장" % ((money%50000)//10000))
print("5천원 : %d장" % ((money%10000)//5000))
print("1천원 : %d장" % ((money%5000)//1000))
print("5백원 : %d장" % ((money%1000)//500))
print("1백원 : %d장" % ((money%500)//100))
