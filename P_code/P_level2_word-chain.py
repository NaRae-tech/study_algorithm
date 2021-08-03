def solution(n,words):
    for i in range(1, len(words)):
        if words[i][0]!=words[i-1][-1] or words[i] in words[:i]:
            return [i%n+1, i//n+1]
    return [0,0]

def solutions(n, words):
    already = [words[0]]
    index = 1
    flag = True
    while(index<len(words)):
        if(already[-1][-1]!=words[index][0]):
            flag = False;
            break
        elif words[index] in already:
            flag = False;
            break
        else:
            already.append(words[index])
            index+=1
    if flag==True:
        return [0,0]
    else:
        return [index%n+1, index//n+1]


words=["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
print(solution(3,words))