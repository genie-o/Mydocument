'''
# sum() : 요소값 모두 더하기
t1 = 1,2,3,4,5
print(sum(t1))

# len() : 길이 구하기
print(len(t1))

# max(), min() : 최대값, 최소값 구하기
print(max(t1))
print(min(t1))

# index(요소의 값) : 요소의 인덱스 번호 구하기
print(t1.index(3)) # 숫자 3의 인덱스 번호 구하기

# count(요소의 값) : 요소의 개수 구하기
t1 = 1,1,1,2,2,
print(t1.count(1)) # 숫자 1의 개수 구하기

'''

#문제1. sum()함수를 구현하기 : my_sum()

def sum(*a):
    total=0
    for i in a:
        total += i

        return total

print(sum(1,2,3))



#문제2. max() 함수를 직접 구현하기
#문제3. min() 함수를 직접 구현하기
#문제4. index()함수를 직접 구현하기
#문제5. count()함수를 직접 구현하기
#문제6. replace()함수를 직접 구현하기
