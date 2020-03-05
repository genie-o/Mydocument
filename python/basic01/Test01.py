#한줄주석
'''
여러줄 주석
여러줄
'''
print("hello")
'''
**** 단축키 ****
실행 (run)
	현재 파일 실행 : ctfl + shift + F10
	파일 선택 실행 : alt + shift + F10
	재실행 : shift + F10
주석처리 : ctrl + /
폴더, 새파일 생성 : alt + insert
복제 : ctrl + D
이동 : alt + shift + 위아래 방향
삭제 : ctrl + Y , shift + del
화면 전환 : ctrl + tab
()밖으로 빠져나가기(자동완성) : ctrl + shift + enter
'''
# 출력함수
print("hello")
print(10)
print("hello")

# 줄내림 기능 없애기
print("엔터기능 없애라", end="")
print("없어졌니????")
'''
출력문 내에서 연결하여 출력시,.
    문자 + 문자 --> 문자 붙어서 출력
    문자 , 문자 --> 문자 띄어쓰기 되어 출력
    숫자 + 숫자 --> 연산 결과 출력
    숫자 , 숫자 --> 문자처럼 나란히 연결출력
    문자 , 숫자 --> 띄어쓰기 되어 출력
    문자 + 숫자 --> 에러
'''
print("10+10")
print(10+10)
print("hello" * 10)

print("he'llo")
print('he"llo')
#서로 다른 타입 값을 나열해서 출력할 경우 , 로 이어준다.

print(10, "10")
print("10"+ "10")
