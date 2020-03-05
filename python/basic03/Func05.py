# 파라미터와 인자의 개수, 순서가 일치해야 한다

# 파라미터 순서가 바뀌어도 가능한 바업
# 인자 기입시, 파라미터명=값
def signUp(username, pw, name, gender, email, nation):
    print("username:", username)
    print("pw:", pw)
    print(name)
    print(gender)
    print(email)
    print(nation)

signUp(pw=1234, username="python", name="피카", gender="여성", email="ddd@sss.com",nation="korea")