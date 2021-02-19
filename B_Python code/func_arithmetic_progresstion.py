hanSu = 0;

def checking(a : int):
    strA = str(a)
    if a<100:
        return True
    else:
        if(strA[0]==strA[1]==strA[2]):
            return True
        elif(int(strA[2])-int(strA[1])==int(strA[1])-int(strA[0])):
            return True
        return False

X = int(input())
for i in range(1,X+1):
    if(checking(i)==True):
        hanSu+=1

print(hanSu)