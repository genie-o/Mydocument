

score = [40,78,34,97,68]
# 시험 점수가 60점 이상이면 합격 그렇지 않으면 불합격 출력
# for문으로 만들어보세요.
num=1
for i in score:
    if i >= 60:
        print("%d번 학생의 점수는 %d점으로 합격이다" % (num, i))
    else:
        print("%d번 학생의 점수는 %d점으로 불합격이다" % (num, i))
    num += 1
