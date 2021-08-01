def solution(s):
    zeroCount = 0
    repetition = 0
    while(s!="1"):
        zeroCount += s.count("0")
        temp = s.replace("0", "")
        s= bin(len(temp))[2:]
        repetition+=1
    return [repetition, zeroCount]

s = "110010101001"
print(solution(s))