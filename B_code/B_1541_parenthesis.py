import sys
strinput = sys.stdin.readline()

#숫자는 numbers에 기호는 sign에 넣기
numbers = []
sign = []
number = ""
for i in range (len(strinput)):
    if((strinput[i] == "-") or (strinput[i]== "+")):
        sign.append(strinput[i])
        numbers.append(int(number))
        number = ""
    else:
        number+=strinput[i]
numbers.append(int(number))

index = 0
while(True):
    if(index==len(sign)):
        break
    if(sign[index] == '+'):
        numbers[index] += numbers[index+1]
        del numbers[index+1]
        del sign[index]
    else:
        index+=1

result = 0
for j in range(0,len(sign)):
    numbers[j+1] = numbers[j]-numbers[j+1]
print(numbers[len(numbers)-1])