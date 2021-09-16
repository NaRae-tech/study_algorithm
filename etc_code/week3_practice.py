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

#class exerciese1
class Queue:
    queue = []
    def isEmpty(self):
        return (len(self.queue) == 0)
    def enqueue(self, num):
        self.queue.append(num)
    def dequeue(self):
        if len(self.queue) != 0:
            self.queue.pop()
    def peek(self):
        if len(self.queue) != 0:
            return self.queue[0]
        else:
            return "None"
    def queueSize(self):
        return len(self.queue)

from random import *
def clEx3():
    i = 0
    Q = Queue()
    while i<10:
        num = randint(1,2)
        print("---%d step---" %(i+1))
        if num == 1:
            Q.enqueue(i)
        else:
            num = Q.dequeue()
        print("Current queue: ",Q.queue)
        print("Peek data:", Q.peek())
        print("Queue size:", Q.queueSize())
        i+=1

#class exercise2
class Shelf:
    box = [[],[],[],[]]
    def levelSize(self, num):
        return len(self.box[num])
    def isFull(self, num):
        return (True if self.levelSize(num) == 4 else False)
    def isEmpty(self, num):
        return (True if self.levelSize(num)== 0 else False)
    def addNum(self,num):
        floor = num%4
        if self.isFull(floor):
            print("%d층은 꽉차서 더이상 공간이 없습니다."%(floor++1))
        else:
            self.box[floor].append(num)
    def delNum(self,num):
        floor = -num-1
        if self.isEmpty(floor):
            print("%d층은 비어서 제거할 숫자가 없습니다." %(floor+1))
        else:
            self.box[floor].pop()

def clEx2():
    s = Shelf()
    num =0
    print("-4 <= N <= -1: 각 층의 최근 입력 숫자 제거, 나머지 음수:종료")
    while num>-5:
        num = int(input("0 혹은 양수 입력 :"))
        if num>=-4 and num<=-1:
            s.delNum(num)
        elif num<-4:
            print("종료합니다.")
            break
        else:
            s.addNum(num)
        print("--> 현재 box 상태 : ",s.box)

#class exercise3
class Square:
    def __init__(self, x, y, length):
        self.X = x
        self.Y = y
        self.L = length
        self.point1 = [self.X,self.Y]
        self.point2 = [self.X+self.L,self.Y]
        self.point3 = [self.X,self.Y+self.L]
        self.point4 = [self.X+self.L,self.Y+self.L]
class CommonArea:
    def __init__(self,s1,s2):
        if ((s1.point2[0]<=s2.point1[0] or s2.point2[0]<=s1.point1[0])
        or s1.point3[1]<=s2.point1[1] or s2.point3[1]<=s1.point1[1]):
            self.area = 0.00
        elif s1.X<=s2.X and s1.Y<=s2.Y:
            self.area = abs(s1.point2[0]-s2.point1[0])*abs(s1.point4[1]-s2.point1[1])
        elif s2.X<=s1.X and x2.Y<=s1.Y:
            self.area = abs(s2.point2[0]-s1.point1[0])*abs(s2.point4[1]-s1.point1[1])
        elif s1.X<=s2.X and s1.Y>=s2.Y:
            self.area = abs(s1.point2[0]-s2.point1[0])*abs(s2.point3[1]-s1.point2[1])
        elif s2.X <= s1.X and s2.Y >= s1.Y:
            self.area = abs(s2.point2[0] - s1.point1[0]) * abs(s1.point3[1] - s2.point2[1])

def clEx3():
    for i in range(2):
        print("첫 번째 정사각형의 중심좌표와 한 변의 길이를 입력하세요.")
        x1 = int(input("X좌표 : "))
        y1 = int(input("Y좌표 : "))
        l1 = int(input("한 변의 길이 : "))
        s1 = Square(x1,y1,l1)

        print("\n두 번째 정사각형의 중심좌표와 한 변의 길이를 입력하세요.")
        x2 = int(input("X좌표 : "))
        y2 = int(input("Y좌표 : "))
        l2 = int(input("한 변의 길이 : "))
        s2 = Square(x2,y2,l2)

        print("첫 번째 정사각형의 좌표, 넓이 : ", [x1,y1],l1**2)
        print("두 번째 정사각형의 좌표, 넓이 : ", [x2,y2],l2**2)
        ca = CommonArea(s1,s2)
        print("두 정사각형의 공통 넓이 : ",ca.area)

clEx3()