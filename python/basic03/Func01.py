'''
***함수 function***
def 함수명():
    실행문들...
----------------------
함수명()

def 함수명(매개변수1, 매개변수2,...):
    실행문들...
    return 값
------------------------

변수 = 함수명(인자1, 인자2...)

## 함수의 종류
# 사용자 정의 함수 : 개발자가 직접 작성한 함수
# 내장 함수 (builtins.py)
    print(), input(), len(), range()....
# 메서드 : 클래스 안에 있는 함수를 부르는 이름

함수명 : 소문자로 시작

'''


def showInfo():
    print("함수야!!!!!")

showInfo()

def getNum():
    print("리턴 있다!!")
    return 10

num = getNum()
print(num)


def showName(name):
    print("당신의 이름은 %s 입니다." % name)

showName("피카츄")

def my_sum(num1, num2):
    result = num1 + num2
    return result

result = my_sum(10,20)
print(result)


def my_sub(num1, num2):
    result = num1 - num2
    return result

result = my_sub(30,2)
print(result)


def my_mul(num1, num2):
    result = num1 * num2
    return result

result = my_mul(3,2)
print(result)


def my_div(num1, num2):
    result = num1 / num2
    return result

result = my_div(10/2)
print(result)