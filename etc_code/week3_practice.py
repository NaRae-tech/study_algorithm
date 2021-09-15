#function exercise1
def Fact(num):
    if num <= 0 :
        return 'Error'
    elif num == 1:
        return num
    else:
        return num*Fact(num-1)

#function exerciese2
def input_num():
    num = int(input("2자리 자연수를 입력하세요 : "))
    if 10<= num and num<100:
        return num
    else:
        print("2자리 자연수가 아닙니다. 다시 입력하세요.")
        return input_num()
def mul(num1, num2):
    print("  %d"%num1)
    print("X %d"%num2)
    print("-"*4)
    print("%4d"%(num1*(num2%10)))
    print("%d "%(num1*(num2//10)))
    print("-" * 4)
    return (num1*(num2//10))*10 + (num1*(num2%10))
def ex2():
    num = [0,0]
    for i in [1,2]:
        print("%d. %d번째 2자리 자연수 출력"%(i,i))
        num[i-1] = input_num()
    return ("%4d"%mul(num[0], num[1]))

#function exercise3
import math
def student_grade(n):
    student = 0
    score_list = {}
    while student<n:
        print("학생%d의 점수를 입력하세요: "%student,end="")
        score = int(input())
        if 0<=score and score<=100:
            score_list[student] = score
            student+=1
    return score_list

def grade_calculator(score_list):
    n = len(score_list)
    average = sum(list(score_list.values()))/n
    deviation = 0
    for i in range(len(score_list)):
        deviation+=(score_list[i]-average)**2
    standard_deviation = math.sqrt(deviation/n)
    score_list= sorted(score_list.items(), key=lambda x:x[1])
    print("평균:",average)
    print("표준편차:",standard_deviation)
    print("최고점: 학생%d %d"%(score_list[-1][0], score_list[-1][1]))
    print("최저점: 학생%d %d"%(score_list[0][0], score_list[0][1]))

def ex3():
    n = int(input("학생 수를 입력하세요: "))
    score_list = student_grade(n)
    print("학생 점수 :",list(score_list.values()))
    grade_calculator(score_list)

#function exercise4
def alphaCnt(phone):
    cnt = 0
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for p in phone:
        if p in alpha:
            cnt+=1
    return cnt

def ex4(model):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    phones = {}
    for m in model:
        phones[m] = [len(m), alphaCnt(m)]
    sort_phones = sorted(phones.items(), key=lambda x:(x[1][0],x[1][1],x[0]))
    result = []
    for sp in sort_phones:
        result.append(sp[0])
    return result

#file handlig exercise1
def fEx1():
    f = open("C:/Users/ynr87/PycharmProjects/baekjoon/test.txt",'w')
    f.write("Engine vibrations can harm phones'\nOptical-image stabilisation or closed-loop autofocus systems, it says.\nOwners of scooters and mopeds should also use vibration-dampening mounts\n")
    f.close()

    f = open("C:/Users/ynr87/PycharmProjects/baekjoon/test.txt",'r')
    f2 = open("C:/Users/ynr87/PycharmProjects/baekjoon/test_copy.txt", 'a')
    while True:
        line = f.readline()
        f2.write(line)
        if not line:
            break
    f.close()
    f2.close()

#file handling exercise2
def student(name, midExam, finExam, score):
    average_score = round((midExam+finExam+score)/3,2)
    grade = ""
    if 90<= average_score and average_score<=100:
        grade = "A"
    elif 80<=average_score and average_score<90:
        grade = "B"
    else:
        grade="C"
    return "{n}|{m}|{f}|{s}|{a}|{g}\n".format(n=name, m=midExam, f=finExam, s=score, a=average_score, g=grade)

def fEx2():
    f = open("C:/Users/ynr87/PycharmProjects/baekjoon/student.txt", "a")
    f.write(student('Jerry',90,89,99))
    f.write(student('Eric',56,45,80))
    f.write(student('Sun',20,79,60))
    f.write(student('Jacob',40,39,98))
    f.close()

#file handling exercise3
def search(name):
    f = open("C:/Users/ynr87/PycharmProjects/baekjoon/student.txt",'r')
    flag = False
    while True:
        line = f.readline()
        info = line.split("|")
        if name == info[0]:
            print("average:",info[4], ",grade:",info[5])
            flag = True
            break
        if not line:
            break
    if not flag:
        print("없음")
fEx2()
search('Sun')
search('Jacob')
search('Yuna')