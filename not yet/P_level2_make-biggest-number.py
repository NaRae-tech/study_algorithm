def first(num):
    return int(str(num)[0])

def second(num):
    snum = str(num)
    if len(snum)==1:
        return int(snum[0])
    else:
        return int(snum[1])

def third(num):
    snum = str(num)
    if len(snum) == 1:
        return int(snum[0])
    elif len(snum)==2:
        return int(snum[1])
    else:
        return int(snum[2])

def solution(numbers):
    numbers.sort(key=lambda x:(first(x),second(x),third(x)), reverse=True)
    numbers = list(map(str,numbers))
    print(numbers)
    return ''.join(numbers)

numbers=[99,999,9,998,989]
print(solution(numbers))