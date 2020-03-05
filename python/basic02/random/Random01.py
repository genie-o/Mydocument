'''
*** Random 난수 ***
*seed : 임의로 선택하는 것처럼 만들어주는 숫자
'''
import random
num = random.randint(1,5)
print(num)

# 0~1 사이의 실수 형태인 난수
print(random.random())

# 리스트의 값들중 하나를 무작위로 추출
lst = [10,20,30,40,50]
num2 = random.choice(lst)
print(num2)

# 원하는 만큼의 리스트 원소들을 무작위로 추출
num3 = random.sample(lst, 3)
print(num3)

# 리스트를 무작위로 섞어준다
print(lst)
random.shuffle(lst)
print(lst)


# 문제1. 동전던지기. 앞면(0), 뒷면(1) 인지 출력

coin = [0,1]
up = random.choice(coin)
if coin ==0:
    print("앞면")
else:
    print("뒷면")

# 문제2. 가위(0), 바위(1), 보(2) 게임

'''
컴퓨터와 가위바위보 대결하기
컴퓨터는 임의의 값을 가지고,
플레이어는 입력을 하여 서로 비교 한 후,
플레이어가 이겼는지 비겼는지 졌는지 출력
'''

com = random.randint(0,2)
#com=[0,1,2]
player=int(input("0=가위,1=바위,2=보 일떄 숫자로 입력하세요"))
com=random.choice(com)

print("컴퓨터",com)
print("플레이어",player)

if com==player:
    print("비겼습니다")
elif com>player:
    print("졌습니다")
else:
    print("이겨습니다")