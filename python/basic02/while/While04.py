#ATM 기계
menu = """
    *** 글로벌 은행 ATM ***
    1. 입금
    2. 출금
    3. 잔액조회
    4. 계좌 이체
    5. 종료
"""
my_money=100000
# 1단계 : 메뉴 번호 선택하면, 메뉴 이름 출력
"""
print("*** 글로벌 은행 ATM ***")
print("1. 입금")
print("2. 출금")
print("3. 잔액조회")
print("4. 계좌이체")
print("5. 종료")
while True:
    menu=int(input("메뉴 번호 선택 하여주세요!"))
    if menu == 1:
        menu1="입금"
        print(menu1)
    elif menu ==2:
        menu2 ="출금"
        print(menu2)
    elif menu ==3:
        menu3="잔액조회"
        print(menu3)
    elif menu ==4:
        menu4 = "계좌이체"
        print(menu4)
    elif menu ==5:
        menu5 = "종료"
        print(menu5)
        break
    else:
        print("메뉴에 없는 번호를 선택하셨습니다. 다시 입력해주세요")
"""
# 2단계: 메뉴별 기능 구현하기
print("*** 글로벌 은행 ATM ***")
print("1. 입금")
print("2. 출금")
print("3. 잔액조회")
print("4. 계좌이체")
print("5. 종료")
while True:
    menu=int(input("메뉴 번호 선택 하여주세요!"))
    if menu == 1:
        menu1="입금"
        print(menu1)
        insert=int(input("입금할 금액을 입력하세요"))
        my_money+=insert
        print("입금되었습니다")
        print("계좌의 잔액은 %d 원 입니다" % (insert+my_money))
    elif menu ==2:
        menu2 ="출금"
        print(menu2)
    elif menu ==3:
        menu3="잔액조회"
        print(menu3)
    elif menu ==4:
        menu4 = "계좌이체"
        print(menu4)
    elif menu ==5:
        menu5 = "종료"
        print(menu5)
        break
    else:
        print("메뉴에 없는 번호를 선택하셨습니다. 다시 입력해주세요")

# 3단계: id 와 pw 입력받아서 로그인 하면 서비스 이용가능하게 만들기
# 4단계: id 와 pw 3회 오류시 프로그램 강제 종료

#Up,Down 게임

'''
컴퓨터로부터 1 ~ 100 사이의 임의의 숫자를 입력받고,
우리는 그 숫자를 맟춰 보자
총 기회는 10번 기회를 모두 소진하면 종료!
슷자를 맞췄을 경우 "축하합니다" 종료
기회가 끝날을 경우 "실패.." 종료
'''