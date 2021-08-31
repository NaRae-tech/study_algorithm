def solution(word):
    answer = 0
    for i,p in enumerate(word):
        answer+= ("AEIOU".index(p) *781//5**i+1)
    return answer

from itertools import product
def solution1(word):
    dic = []
    for i in range(5):
       for p in product("AEIOU", repeat = i+1):
           dic.append("".join(p))
    dic.sort()

    return dic.index(word)+1

def solution2(word):
    answer = 0
    dic = {'A':1, 'E':2, 'I':3, 'O':4, 'U':5}

    words = [0,0,0,0,0]
    for i in range(len(word)):
        words[i] = dic[word[i]]

    temp = 1
    for i in range(len(words)-1,-1,-1):
        if words[i]!=0:
            answer += (temp*(words[i]-1)+1)
            print(temp, answer)
        temp = temp*5+1

    return answer

word = "AAAE"
print(solution(word))