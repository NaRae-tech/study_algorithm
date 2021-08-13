def solution(s):
    answer = []
    dic = {chr(a+64):a for a in range(1,27)}
    index = 27
    while s:
        temp = 1
        while s[:temp] in dic and temp<=len(s):
            temp+=1
        temp-=1
        if s[:temp] in dic:
            answer.append(dic[s[:temp]])
            dic[s[:temp+1]] = index
            index+=1
        s = s[temp:]
    return answer

def solution2(s):
    answer = []
    dict = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5,
            'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
            'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15,
            'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
            'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
    index = 27

    s = list(s)
    while not(not s):
        for i in range(len(s),0,-1):
            temp = ''.join(s[:i])
            if temp in dict:
                answer.append(dict[temp])
                if i<len(s):
                    dict[temp+s[i]] = index
                    index+=1
                del s[:i]
                break
    return answer

print(solution("TOBEORNOTTOBEORTOBEORNOT"))