# 매개변수(파라미터) def 함수명(매개변수/파라미터, ...) :
#       함수 정의부분에 정의됨. 인자를 받아주는 지역변수
#       매개변수 == 파라미터 == parameter

# 인자 : 함수명(인자, 인자...) : 함수 호출할 때 던져주는 데이터
#       인자 == 인수 == 인자값 == 인수값 == arguments == 매개변수


# 파라미터와 인자의 개수, 순서가 일치해야 한다.
# 파라미터의 초기값 넣어주기.
# 초기값이 파라미터에 지정되어 있으면, 인자를 생략 가능하다.
# 인자가 생략되면 초기값이 적용된다.
# 초기값이 있는 파라미터는 파라미터 중에 가장 뒤에 위치해야 한다.

def signUp(username, pw, name, gender, email, nation):
    print(username)
    print(pw)
    print(name)
    print(gender)
    print(email)
    print(nation)

signUp("python", 1234, "피카", "여성", "ddd@sss.com","korea")

