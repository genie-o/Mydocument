#문제1. 카페 주문 프로그램

'''
    메뉴를 출력하고, 주문을 계속 받는 프로그램
    종료를 선택하면 프로그램 종료하고 총 합계를 출력해세요
    menu
        *** 글로벌 카페 ***
        1. 아메리카노 : 2000원
        2. 카페라떼 : 30000원
        3. 자바침 프라프치노 : 4500원
        4. 화이트 모카라뗴 : 4000원
        5. 종료
'''

"""
print("*** 글로벌 카페 ***")
print("1. 아메리카노 : 2000원")
print("2. 카페라떼 : 3000원")
print("3. 자바침 프라프치노 : 4500원")
print("4. 화이트 모카라뗴 : 4000원")
print("5. 종료")

a=2000
b=3000
c=4500
d=4000
total=0
while True:
    order =int(input("주문할 메뉴의 번호를 입력하세요"))
    if order ==1:
        total+=2000
        print(total)
    elif order ==2:
        total+=3000
        print(total)
    elif order ==3:
        total+=4500
        print(total)
    elif order==4:
        total+=4000
        print(total)
    else:
        order==5
        print("주문을 종료하겠습니다")
        break
        
        12345가 아닐 경우 예외처리 하기 
"""
#문제2. 커피 자판기

'''
커피는 10잔만 존재
1. 돈을 입력받는다(커피값:300원 고정)
2. 300원 이상 입력, "거스름돈은??? 입니다. 맛있게 드세요 !" 출력
3. 300원 이하 입력,"돈이 부족합니다
4. 300원 입력, "맛있게 드세요"
커피 10잔이 다 소진되면 프로그램 종료 
'''
"""
i=0
while i<=10:
    num = int(input("주문하시려면 돈을 넣어주세요!"))
    if num == 300:
        print("맛있게 드세요")
    elif num > 300:
        print("거스름돈은?"%num)

    else:
        print("돈이부족합니다")
"""

coffee=10
while True:
    if coffee==0:
        print("커피 매진 종료 하겠습니다")
        break
    coin=int(input("돈을 넣으세요:(프로그램종료:-1) : "))
    if coin >= 300:
        print("거스름돈은 %d 원 입니다 맛있게 드세요"  % (coin-300))
        coffee -= 1
    elif coin == 300:
        print("맛있게 드세요")
        coffee -= 1
    elif coffee <300:
        print("돈이부족합니다")
    elif coffee == -1:
        print("시스템 종료")
        break