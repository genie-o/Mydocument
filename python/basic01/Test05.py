# 문자열 관련 함수

# 문자열 바꾸기 : replace()
str = "apple tree"
print(str)
str = str.replace("apple", "lemon")
print(str)

# 문자열 나누기 : split()
a,b,c,d,e = "1 2 3 4 5".split()
print(a)
str1 = "Global,Institute"
a,b = str1.split(',')
print(a)
print(b)

# 문자열 길이 : len()
str = "sfjadljflksjdfkajdlkfj"
print(len(str))


# 문자 개수 구하기 : count()
print(str.count('f'))


name = "Global IT"
# 문자의 위치 알려주기(1) : find()
print("="*10)
print(name.find('o'))  # 인덱스번호 리턴
print(name.find('z'))  # 찾는값이 없으면 -1 리턴
# 문자의 위치 알려주기(2) : index()
print("="*10)
print(name.index('o'))  # 인덱스번호 리턴
#print(name.index('z'))  # 찾는값이 없으면 에러 발생!

str = "Apple Tree"
# 소문자를 대문자로 바꿔주기 : upper()
str = str.upper()
print(str)

# 대문자를 소문자로 바꿔주기 : lower()
str = str.lower()
print(str)

# 공백 지우기 : strip(), lstrip(), rstrip()
t = "        py th on      "
print(t)
print(t.lstrip())
print(t.rstrip())
print(t.strip())