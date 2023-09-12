scores = []

count = int(input("총 학생수를 입력하세요: "))

for i in range(1, count + 1):
    score = []
    kor = int(input("학생{0}의 국어 점수를 입력하세요: ".format(i)))
    score.append(kor)
    mat = int(input("학생{0}의 수학 점수를 입력하세요: ".format(i)))
    score.append(mat)
    eng = int(input("학생{0}의 영어 점수를 입력하세요: ".format(i)))
    score.append(eng)
    scores.append(score)

for i, score in enumerate(scores):
    total = 0
    for s in score:
        total += s
    print("학생{0} => 총점: {1}, 평균: {2:.2f}".format(i + 1,total, total / len(score)))