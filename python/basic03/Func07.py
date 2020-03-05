# 예상할 수 없는 함수
'''
def 함수명(*파라미터):
    실행문들.....

'''
# 숫자를 원하는 만큼 인자로 입력해 함수를 호출하면
# 모든 숫자를 더해서 총 합계를 돌려주는 함수를 만들자.

def sum(*num):
    tot = 0
    for i in num:
        tot += i
    return tot

print(sum(10,20,30))

# op : 연산자 기호, *num 연산하고 싶은 수들
def calc(op, name, *num, age=0):
    if op == '+':
        tot = 0
        for i in num:
            tot += i
    elif op == 'sub':
        tot = 0
        for i in num:
            tot -= i
    elif op == 'mul':
        tot = 1
        for i in num:
            tot *= i
    print("Age =", age)
    return tot

print(calc("mul", 1,2,3,4,5, "홍길동"))
