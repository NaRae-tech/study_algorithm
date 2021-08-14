def compare(temp):
    answer = []
    now = temp[0]
    count = 1
    print(temp, temp[1:]+[''])
    for a, b in zip(temp, temp[1:]+['']):
        if a==b:
            count+=1
        else:
            answer.append([count, now])
            count, now = 1, b
    return sum(len(word)+(len(str(cnt)) if cnt>1 else 0) for cnt,word in answer)

def solution(s):
    answer = [len(s)]
    temp = []
    for i in range(1, len(s)//2+1):
        temp = [s[a:a+i] for a in range(0,len(s),i)]
        answer.append(compare(temp))
        temp = []
    return min(answer)

def check(s):
    answer = ""
    now = s[0]
    count = 1
    for i in range(1, len(s)):
        if now==s[i]:
            count+=1
        else:
            if count != 1:
                answer+=str(count)
            answer+=now
            now = s[i]
            count = 1
    if count != 1:
        answer += str(count)
    answer += now
    return answer
def solution2(s):
    answer = []
    temp = []
    for i in range(1, len(s)+1):
        j = 0
        while i*j<len(s):
            temp.append(s[i*j:i*(j+1)])
            j+=1
        result = check(temp)
        if result not in answer:
            answer.append(len(result))
        temp = []
    print(answer)
    return min(answer)

s="ababcdcdababcdcd"
print(solution(s))