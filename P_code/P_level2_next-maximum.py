n = 78

binN = bin(n).count('1')
answer = n+1
while(True):
    if(binN==bin(answer).count('1')):
        break
    answer+=1
print(answer)