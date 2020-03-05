'''
*** 변수의 scope ***
변수의 종류 (선언 위치에 따른)
    1. 전역변수 global variable
        선언 위치 : 함수 밖
        유효 범위 : 프로그램이 종료될 때 까지 유효
                    함수 안에서 사용할 시 참조형으로만 사용 가능.
                    함수 내에서 변경 불가능!!

                * 함수 내에서 전역변수 값을 변경하는 방법
                    #1. 리턴값 이용하기
                    #2. global 키워드 이용하기 (비추천)


    2. 지역변수 local variable
        선언 위치 : 함수 안
        유효 범위 : 함수 안에서만, 함수가 종료될 시 소멸
                    함수 밖에서 사용 불가
'''
#전역변수
# num = 10
# print(num)

##################
# def func(num1): # 지역(매개)변수
#     num1=num1+1
#     print(num1)
#     return num1
##################

# num = func(num) # 전역변수 던지기
# print(num) # 전역변수 출력

# print(hello) 지역변수는 외부에서 접근 불가


num = 5
print("전역:" , num)
def func1():
    global num # 전역의 num을 함수에서 변경가능하게 사용할게~ 선언함.
    num = num + 1
    print(num)

func1()
print("전역:" , num)
