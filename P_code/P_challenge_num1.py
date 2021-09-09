def solution(numbers):
    target = [i for i in range(10)]
    for num in numbers:
        if num in target:
            target.remove(num)

    return sum(target)

numbers = [1,2,3,4,6,7,8,0]
print(solution(numbers))