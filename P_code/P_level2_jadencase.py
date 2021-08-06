def solution(s):
    sL = list(map(str, s.lower().split(" ")))
    for i in range(len(sL)):
        sL[i] = sL[i].capitalize()
    return " ".join(sL)

s ="aaa  aaaasa"
print(solution(s))