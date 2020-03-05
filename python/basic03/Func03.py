'''
문제1. 계산기 : calc()
사칙연산을 모두 수행하여 결과를 보여주는 프로그램 만들기
단, 사용자에게 종료여부를 물어서 y를 입력하면 프로그램 종료.
n을 입력하면 계속 계산

콘솔출력에 )
정수1 입력:     10
정수2 입력:     20
덧셈 : 30
뺄셈 : -10
곱셈 : 200
나눗셈 : 0.5

종료하시겠습니까? n

정수1 입력:
정수2 입력:
덧셈
뺄셈
곱셈
나눗셈

종료하시겠습니까? y
프로그램 종료!

'''
'''
d1 = int(input("정수1입력:"))
d2 = int(input("정수2입력:"))

def calc(d1, d2):
    result = d1+d2
    return result

result = calc(d1, d2)
print("덧셈", result)

def calc(d1, d2):
    result = d1-d2
    return result

result = calc(d1,d2)
print("뺄셈", result)

def calc(d1, d2):
    result = d1*d2
    return result

result = calc(d1,d2)
print("곱셈", result)

def calc(d1, d2):
    result = d1/d2
    return result

result = calc(d1,d2)
print("나눗셈:", result)
'''


#선생님 답

def calc():
    while True:
        num1 = int(input("정수1 입력:"))
        num2 = int(input("정수2 입력:"))
        print("덧셈:", num1+num2)
        print("뺄셈:", num1-num2)
        print("곱셈:", num1*num2)
        print("나눗셈:", num1/num2)

        # y_n = input("종료하시겠습니까?(y/n):")
        # if y_n.lower() == "y":
        #     print("프로그램 종료")
        #     break
        # else:
        #     continue

        res = check()
        if res == 1:
            print("프로그램 종료")
            break
        elif res == 0:
            continue
        elif res == -1:
            res = check()



def check():
    result = False
    y_n = input("종료하시겠습니까?:")
    if y_n.lower() == "y":
        result = 1
    elif y_n.lower() == "n":
        result = 0
    else :
        check()
    return result

#함수실행
calc()



'''
문제2. 로그인프로그램 : login()
사용자로부터 id와 pw를 입력받아
로그인메세지 출력
id가 틀리면 "id는 존재하지 않는 아이디입니다"
pw가 틀리면 "비밀번호가 다릅니다.
둘 다 일치하면, "id님 환영합니다." 출력

'''

def login(id, pw):
    if id == db_id:
        if pw == db_pw:
            print("%s님 환영합니다." % db_id)
        else:
            print("비밀번호가 다릅니다.")
    else:
        print("%s는 존재하지 않는 id 입니다. % id")


db_id = "python"
db_pw = "1234"
id = input("아이디 입력:")
pw = input("패스워드 입력:")


login(id, pw)