# 무한적으로 숫자를 입력받아 출력하는 While 문 만들어보자
# 단, 숫자 9를 입력하면 while 문 종료

'''
while True:
    num=int(input("숫자입력:"))
    print("num=%d" %num)
    if num == 9:       # 종료 시점 반드시 ㅍ필요함
        print("while 문 종료")
        break
'''

import time
while True:
    print("시작을 원하면 enter를 눌러주세요")
    input()
    print("게임 시작")
    time.sleep(3)
    print("게임종료")
    break