def solution(N,A,B):
    answer = 0
    while A!=B:
        answer+=1
        A,B = (A+1)//2, (B+1)//2
    return answer

def solution1(N,A,B):
    return ((A-1)^(B-1)).bit_length()

def solution2(N,A,B):
    rangeA = 0
    rangeB = 0

    for i in range(1,21):
        if 2**(i-1)<A and 2**i>=A:
            rangeA = i;
        if 2**(i-1)<B and 2**i>=B:
            rangeB = i;
        if rangeA!=0 and rangeB!=0:
            break

    if rangeA!=rangeB:
        return max(rangeA, rangeB)
    else:
        A -= 2**(rangeA-1)
        B -= 2**(rangeB-1)
        return solution(N,A,B)

N = 16
A = 17
B = 18
print(solution(N,A,B))