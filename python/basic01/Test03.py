'''
자료형 (data type)
1) 숫자형
    1. 정수 : int (integer)
            파이썬 2.x 버전 : int, long
            파이썬 3.X 버전 : int
    2. 실수 : float
            파이썬 2.x 버전 : 5000 / 3 = 1666
            파이썬 3.x 버전 : 5000 / 3 = 1666.666~

2) 참/거짓형 : bool (bo
olean)
            True / False (첫글자 대문자)

3) 군집자료형
    1. 문자열형 : str (string)
    2. 리스트 : list
    3. 튜플 : tuple
    4. 딕셔너리 : dict (dictionary)
    5. 집합 : set


*** 변수 variable ***
    데이터타입 기술 X (동적 언어)

    type() : 데이터 타입을 돌려주는 함수

    변수 명명규칙
    num != Num
    n1um(o)    1num(x)
    특수문자 _  my_num  muNum


'''

num = -513
num2 = -3.14
s1 = 'h'
print(num)
print(type(num))
print(type(num2))
print(type(s1))



'''
입력을 받는 함수 : input()
    변수 = input("콘솔에 띄워줄 메세지")
'''

#name = input("이름을 입력하세요.")
# print(name)


'''
형변환 cating, convert

    문자 ---> 정수
        int("10")
        
    문자 ---> 실수
        float("3.14")
    
    정수/실수 --> 문자
        str(정수/실수)
'''
'''
# 입력받아온 데이터는 문자열(str)로 리턴해준다.
age = int(input("나이 입력 : "))
print("당신의 내년 나이는 %d 살 이네요." % (age+1))
'''

# 국어 수학 영어 점수를 입력받아, 총점과 평균을 출력하세요. % 포매팅 사용

k = int(input("국어 점수 : "))
m = int(input("수학 점수 : "))
e = int(input("영어 점수 : "))
print("총점은 %d 이다." %(k+m+e))
print("평균점수는 %d 이다." %((k+m+e)/3))











