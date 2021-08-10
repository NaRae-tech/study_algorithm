import re
from collections import Counter
def solution(s):
    sc = Counter(re.findall('\d+',s))
    return list(map(int, [k for k,v in sorted(sc.items(),key=lambda x:x[1],reverse=True)]))

import re
def solution2(s):
    answer = []

    tt = []
    temp = ""
    for i in range(1,len(s)-1):
        if s[i]=="{":
            temp = ""
        elif s[i]=="}":
            tt.append(temp)
        elif s[i]=="," and s[i+1]=="{":
            pass
        else:
            temp+=s[i]
    tuple = []
    for item in tt:
        tuple.append(list(map(int,item.split(','))))

    tuple.sort(key=lambda x:len(x))
    for item in tuple:
        for element in item:
            if element not in answer:
                answer.append(element)
    return answer

s="{{111,20},{20}}"
print(solution(s))