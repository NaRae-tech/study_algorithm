def solution(w,h):
    answer = 0
    if w<=1 or h<=1:
        return 0
    elif w==h:
        return w*h-w
    else:
        for i in range(1, w):
            answer+=(h*i//w)
        return answer*2

from math import gcd
def solution(w,h):
    return w*h-(w/gcd(w,h)+h/gcd(w,h)-1)*gcd(w,h)

w = 3
h= 4
print(solution(w,h))