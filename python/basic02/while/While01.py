'''
반복문 : while , for

*** while ***
구조
    #1. 반복 횟수를 알때 지정 
    while 조건식 :
        실행문...
        증감식

    #2. 무한 반복
    while True:
        실행문.....
        // 종료 시점
        if 조건문:
            break
'''

#10회 반복
"""
i=0;
while i<10:
    print("hello")
    i+=1
"""

# 문제1. 0~3까지 출력
"""
i=0
while i<4:
    print("%d"%i)
    i+=1
"""
# 문제2. 1~10 사이의 홀수 출력
'''
i=1
while i<=10:
    if i%2 ==1:
         print("%d"%i)
   i += 1
'''

# 문제3. 0~100 사이의 수중 10 단위로 출력 (0,10,20,30...)

i=0
while i<=10:
    if i == 0:
        print("%d" %i)
    else:
        print("%d"%(i*10))
    i+=1

# 문제4. 1~10 까지의 모든 수를 더한 합을 출력
"""
i=1
sum=0
while i<11:
    sum += 1
    i += 1
print("sum =%d" %sum)
"""
# 문제5. 1~20 까지지의 짝수만 모둔 더한 값 출력
"""
i=1
sum=0
while i<=20:
    if i%2 ==0:
        sum += i
    i+=1
print("sum=%d" %sum)
"""
# 문제6. 숫자를 5번 입력받고, 입력 받은 수를 모두 더한 값을 출력
"""
i=0
total=0
while i<5:
    num=int(input("숫자입력:"))
    total += num
    i += 1
print("total=%d" %total)
"""











