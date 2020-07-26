kor_score = [49,79,20,100,80]
math_socre = [43,59,85,30,90]
eng_score = [49,79,48,60,100]

midterm_score = [kor_score,math_socre,eng_score]

print(midterm_score[0][2])

student_score = [0,0,0,0,0]
i = 0
for subject in midterm_score:

    for score in subject:
        #각 학생마다 개별로 과목점수를 저장
        student_score[i] += score
        #학생 인덱스 구분
        i += 1
    #과목이 바뀔때 마다 학생 인덱스 초기화
    i = 0
else:
    print(student_score)
    # 학생별 점수를 언패킹
    a, b, c, d, e = student_score
    student_average = [int(a/3), int(b/3), int(c/3), int(d/3), int(e/3)]
    print(student_average)


