# 리스트 관련 함수들...

# 요소 추가하기 : append()
lst = []
lst.append(1)
lst.append("abc")
print(lst)
print(type(lst))

#리스트 확장 : exten()
lst1 = [1,2,3]
lst2 = [4,5,6]
#lst2.extend(lst2)
#print(lst1)

lst1.append(lst2)
print(lst1)

# 요소 삽입하기 : insert(인덱스번호, 삽입할데이터)
lst = [1,2,3]
lst.insert(1,10)
print(lst)

# 요소 제거하기 : remove(데이터)
lst.remove(10)
print(lst)