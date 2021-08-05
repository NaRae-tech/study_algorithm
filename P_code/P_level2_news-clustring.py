#방법 1
import re
def solution(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if not re.findall('[^a-zA-Z]+',str1[i:i+2])]
    str2 = [str2[i:i + 2].lower() for i in range(len(str2) - 1) if not re.findall('[^a-zA-Z]+', str2[i:i + 2])]

    common = set(str1)&set(str2)
    union = set(str1)&set(str2)

    if len(union) == 0:
        return 1*65536

    common_count = sum([min(str1.count(co),str2.count(co)) for co in common])
    return int((common_count/(len(str1)+len(str2)-common_count))*65536)

#방법 2
def solutions(str1, str2):
    answer =0

    str1=str1.lower()
    str2=str2.lower()
    str1L = []
    str2L = []
    for i in range(len(str1) - 1):
        if str1[i].isalpha() and str1[i + 1].isalpha():
            str1L.append(str1[i] + str1[i + 1])
    for i in range(len(str2) - 1):
        if str2[i].isalpha() and str2[i + 1].isalpha():
            str2L.append(str2[i] + str2[i + 1])

    if len(str1L) == 0 and len(str2L) == 0:
        return int(1 * 65536)
    if sorted(str1L) == sorted(str2L):
        return int(1 * 65536)

    temp = list(set(str1L)&set(str2L))
    common = []
    for item in temp:
        repetition =  min(str1L.count(item), str2L.count(item))
        for i in range(repetition):
            common.append(item)
    print(common)
    answer = len(common)/(len(str1L)+len(str2L)-len(common))
    return int(answer*65536)

str1 = "hand shake"
str2 = "HAND"
print(solution(str1,str2))