'''
자료형
    숫자형      : int, float
    참/거짓형   : bool
    군집자료형  : str, list, tuple, dict, set

*** list 리스트 ***
여러개의 값을 하나로 묶어서 저장할 수 있는 데이터타입
구조 :
    변수명 = [요소1, 요소2, 요소3,...]
특징 :
    다양한 데이터 타입을 섞어서 하나로 묶을 수 있다.
    수정가능 (mutable)
    크기 제한 없다.
구분 기호 : []
'''
nums = [1,2,3,4,5]
print(nums)
# 빈 리스트
a = []
b = list()
print(type(a))
c = ["python", "class"]
print(c)
d = [1,2,"python",'c',3.14]
print(d)

#리스트는 인덱스 번호를 가지고 있다.
nums = [1,2,3,4,5]
print(nums)
print(nums[0])
print(nums[3])
print(nums[-5])

num2 = [ [1,2,3], [4,5,6], [7,8,9] ]
print(num2[0])
print(num2[0][2])

num3 = [1,2,3,[4,5,6],7]
print(num3[3][0])
print(num3[2])
print(num3[4])

num4 = [1,2,3,["a","b","c"],4,5]
print(num4[2:5])
print(num4[3][0:2])

# 리스트 요소 변경
lst = [1,2,3]
lst[0] = 10
print(lst)

lst = [1,2,3]
# 인덱스 번호 1번의 요소를 'a','b','c'로 바꿔보자
lst[1] = ['a','b','c']
print(lst)

lst[1:2] = ['a','b','c']
print(lst)

lst = [1,2,3]
lst[1] = 'a','b','c'
print(lst)







