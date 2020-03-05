# 리스트 속성
# in 연산자 포함하는지 안하는지에 따른 참 거짓 결과가 출력됨

list=[10,20,30,"abc","def"]
if 10 in list:
    print("10이 존재함")

print("ad"in list)  # False
print("ad" not in list)  # True

list =[1,2,3,[4,5,6]]
list[-1][-1]=100
print(list)

#리스트 연산자
# 0이 다섯개 들어간 list 만들어줌
list=[0]*5
print(list)

# + 연산자
list1 = [1,2,3]
list2 = [4,5,6]
print(list1+list2)
list1.extend(list1)

print(list[0]+list2[1])