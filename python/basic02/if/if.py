'''
# 제어문
    1) 조건문 : if
    2) 반복문 : while, for
    3) 보조제어문 : break, continue


1) 조건문 : if
    구조
        if 조건문 :
            실행문들...
            실행문들..
        ---------------
        if 조건문 :
            실행문들...
        else:
            실행문들...
        ---------------
        if 조건문 :
            실행문들...
        elif 조건문
            실행문들..
        elif 조건문
            실행문들..

    # 들여쓰기 indentation
        spacebar 4번 == tab키 1번

'''

score = 70
if score >= 60:
    print("합격")
else:
    print("불합격")

# True : 1, False : 0
result = int(score/60)
if result:
    print("result 합격")
else:
    print("result 불합격")

# 문제1. 정수 1개를 입력받아, 그 수가 '양수'인지 '음수'인지 출력해보세요
a = int(input("정수를 입력하세요 :"))
if a >= 0:
    print("양수")
elif a < 0:
    print("음수")

# 문제2. 정수 1개를 입력받아, 그 수가 "짝수"인지 "홀수"인지 출력해보세요.
b = int(input("정수를 입력하세요 :"))
if (b%2)>=1:
    print("홀수")
else:
    print("짝수")


# 문제3.  id와 pw를 입력받아 모두 일치하면 "(id)님이 로그인되었습니다." 출력
#          불일치하면 "아이디와 비밀번호를 확인해주세요" 출력
db_id = "python"
db_pw = "1234"

id = input("id를 입력하세요 : ")
pw = input("pw를 입력하세요 : ")

if id==db_id and pw==db_pw:
    print("%s 님이 로그인되었습니다." % id)
else:
    print("아이디와 비밀번호를 확인해주세요.")



# 문제4. 주민번호를 입력받아, "여성" / "남성"을 출력해보세요.
joo = input("주민번호13자리를 입력하세요")
if joo[7] == "1" or joo[7] =="3":
    print("남성")
elif joo[7] == "2" or joo[7] =="4":
    print("여성")



# 문제5. 사용자로부터 키를 입력받아, 키가 150 이상이면 " 놀이기구 이용가능해요" 출력
#        140 미만이면, 질문 : 부모님 모시고 왔니? 물어보고 답변은 (yes:1, no:0)받아
#        1 --> "이용가능해 재밌게 놀아"
#        0 --> "부모님 모시고 다시 오렴"

key = int(input("키입력"))
if key >= 150:
    print("놀이기구 이용 가능해요")
else:
    answer =input("부모님 모시고 왔니 ? ")
    if answer == 1:
        print("이용가능해 재밌게 놀아")
    else:
        print("부모님 모시고 다시오렴")


# 문제 6. 학점 처리 프로그램
'''
이름과 국어 영어 수학 3과목에 대한 점수를 입력받아
총첨, 평균, 학점을 구해보세요
단, 평균은 소수점 이하 한자리까지 표현
학점기준 : 90점이상 A 
           80점이상 B
           70점이상 C
           60점이상 D
           그 이해 F
'''

n = str(input("이름:"))
k = int(input("국어:"))
e = int(input("영어:"))
m = int(input("수학:"))
tot = k+e+m
avg = tot/3
hak = ''
if avg >= 90:
    hak = 'A'
if avg >= 80:
    hak = 'B'
if avg >= 70:
    hak = 'C'
if avg >= 60:
    hak = 'D'
else:
    hak = 'F'

print("%s의 총점은 %d 이고, 평균은 %.1f 이며, 학점은 %s입니다." % (n, tot, avg, hak))