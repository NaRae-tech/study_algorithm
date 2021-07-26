n = 123

#방법1
def sum_digit(number):
    if(number<10):
        return number
    return (number%10) + sum_digit(number//10)
print(sum_digit(n))

#방법2
print(sum([int(i) for i in str(n)]))

#방법3
N = list(str(n))
answer = 0
for item in N:
    answer+=int(item)
print(answer)