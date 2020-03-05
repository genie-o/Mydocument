#문제1. 5개의 요소를 가지고 있는 리스트를 하나 만들고,
#       인덱스 번호 2개를 입력받고, 해당 인덱스 번호에 자리한 값을 교환해보자

'''
list=[10,20,30,40,50]
num1=int(input("인덱스1 번호(0~4)를 입력하세요"))
num2=int(input("인덱스2 번호(0~4)를 입력하세요"))
tmp =list[num1]
list[num1]=list[num2]
list[num2]=tmp
print(list)
'''

#문제2. 리스트가 가지고 있는 다양한 함수를 이용해보세요
'''
list1=[1,3,5,4,2]
#
[5,4,3,2,1] 로 만들어 보세요
print(list1)
sort / reverse 
'''

#문제3.아래 리스트를 활용하여 주어진 요소를 출력해보세요
list2=["Global",["IT",[1,3,5,7,9],["Even",[0,2,4,6,8]]]]
# "Global" 출력
print(list2[0])
# 숫자 3 출력
print(list2[1][1][1])
# 숫자 8 출력
print(list2[1][2][1][4])

#문제4. 아래와 같이 출력해보세요

'''
===============
    파이썬
===============
자료형*
제어문***
입출력****
클래스******

'''
subject =["자료형","제어문","입출력","클래스"]
level=[1,3,4,6]
#* 곱하기 를 해서 찍힘

print(subject[0],"*"*level[0])
print(subject[1],"*"*level[1])
print(subject[2],"*"*level[2])
print(subject[3],"*"*level[3])






























