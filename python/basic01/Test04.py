'''
*** 문자열 str ***
    '문자열' "문자열" """여러줄문자열""" (홑따옴표도 여러줄 문자열 가능)

    문자열 indexing
    0 1 2 3 4
    h e l l o



'''
print("hello python")
print('hello python')
print('''hello 
python''')


memo = """안녕하세요
저는 피카츄입니다.
나이는 100살이에요."""
print(memo)


first = "python"
second = "is easy"
third = first + second
print(first , second, third)


a = "python"
print(a * 10)


str1 = "Global IT"
print(str1[0], str1[1], str1[7])

# hello 문자열을 변수에 저장하고 olleh라고 출력해 보세요

str2 = "hello"
print(str2[4],str2[3],str2[2],str2[1],str2[0])
print(str2[4]+str2[3]+str2[2]+str2[1]+str2[0])


# 문자열은 수정 불가능 immutable

# 문자열 슬라이싱
#   문자열을 나눌 수 있다.
#   변수명[시작번호:끝번호] * 끝번호 포함X, 끝번호 전까지

str3 = "Global Istitute"

print(str3[0:6])
print(str3[:6])
print(str3[7:])
print(str3[:])


str4 = "prigraming"

# programming으로 수정하기

print(str4[0:2] + "o" +str4 [3:6] + "m" + str4[6:])
print(str4[:2] + "o" +str4 [3:7] + "m" + str4[-3:])
str4 = "programming"
print(str4)

# 날짜 잘라보기
import datetime

date = datetime.date.today()
print(date)
print(type(date))


date = str(date)
print(type(date))

year = date[:4]
print(year)

month = date[5:7]
print(month)


print(str(date)[:4])
# month =
print(str(date)[5:7])
# day =
print(str(date)[8:10])

print(year+"년"+month+"월")
print("%s년 %s월" % (year, month))








