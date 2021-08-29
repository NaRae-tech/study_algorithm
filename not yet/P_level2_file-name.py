import re
def solution(files):
    answer = []
    temp = []
    for file in files:
        head, num, tail = "","",""
        for i in range(len(file)-1):
            if 48 <= ord(file[i]) and ord(file[i]) <= 57:
                num += file[i]
                if 48 > ord(file[i - 1]) or ord(file[i - 1]) > 57:
                    head = file[:i]
                if len(num) > 5:
                    num = num[:len(num) - 1]
                    tail = file[i:]
                    break
                if 48 > ord(file[i + 1]) or ord(file[i + 1]) > 57:
                    tail = file[i + 1:]
                    break
        temp.append([head,num,tail])
    temp.sort(key=lambda x:(x[0].lower(),int(x[1])))
    for t in temp :
        answer.append(''.join(t))
    return answer

files = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
print(solution(files))