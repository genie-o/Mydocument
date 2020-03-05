# ATM 기계 문제 --> 함수로 바꿔보기
# 실행: 로그인 -> 서비스이용 (각 메뉴누르면 각 메뉴에 해당하는 함수호출)
menu = """
*** 글로벌 은행 ATM ***
1. 입금
2. 출금
3. 잔액 조회
4. 계좌 이체
5. 종료
"""
db_id = "python"
db_pw = "1234"
pw_count = 3

# 1단계 : 메뉴 번호 선택하면, 메뉴 이름 출력
# 3단계 : 아이디와 패스워드 입력받아서 로그인하면 서비스 이용가능하게 만들기
# 4단계 : 아이디와 패스워드 3회 오류시 프로그램 강제 종료
def deposit(money):
    amount = int(input("입금하실 금액 : "))
    money += amount
    print("%d원이 입금되었습니다." % amount)
    return money

def withdraw(money):
    amount = int(input("출금하실 금액 : "))
    money -= amount
    print("%d원이 출금 되었습니다. " % amount)
    return money

def showAccount(money):
    print("계좌 총 금액 : %d원" % money)

def transfer(money):
    amount = int(input("이체하실 금액 : "))
    whom = input("송금처 이름 : ")
    money -= amount
    print("%s님에게 %d원이 이체되었습니다." % (whom, amount))
    return money

def login():
    global pw_count
    if pw_count == 0:
        print("더이상 로그인을 진행할 수 없습니다. ")
        return -2
    id = input("아이디 입력:")
    pw = input("패스워드 입력:")
    if id == db_id:
        if pw == db_pw:
            print("%s님 환영합니다." % db_id)
            return 1
        else:
            print("비밀번호가 다릅니다.")
            pw_count -= 1
            return login()
    else:
        print("%s는 존재하지 않는 id 입니다." % id)
        return -1

def start():
    my_money = 100000  # 지역변수
    res = login()
    if res == -2:
        print("비밀번호 3회 오류! 비밀번호 재설정하세요...")
        return ##비밀번호 재설정 함수 호출
    if res == 1:
        while True:
            print(menu)
            sel = int(input("원하는 메뉴 입력 : "))
            if sel == 1:
                my_money = deposit(my_money)
            elif sel == 2:
                my_money = withdraw(my_money)
            elif sel == 3:
                showAccount(my_money)
            elif sel == 4:
                my_money = transfer(my_money)
            elif sel == 5:
                print("프로그램 종료!!!")
                break
            else:
                print("메뉴 번호를 확인하시고 다시 선택해주세요!!")

# 프로그램 시작점
start()













