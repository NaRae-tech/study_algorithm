def change(n):
    sn = str(n)
    if len(sn) == 3:
        return sn
    elif len(sn) == 2:
        return sn+sn[0]
    else:
        return sn*3
def solution(numbers):
    numbers.sort(key=lambda x:change(x),reverse=True)
    numbers = list(map(str, numbers))
    print(numbers)
    return ''.join(numbers)

numbers = [99,999,9,988,889,8,34]
print(solution(numbers))