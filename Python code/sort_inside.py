import sys
string = sys.stdin.readline()
stringL= len(string)
stringList = [int(string[i]) for i in range(0,stringL-1)]
for i in range(0,stringL-1):
    for j in range(0, stringL-1):
        if(stringList[i]>stringList[j]):
            temp = stringList[i]
            stringList[i] = stringList[j]
            stringList[j] = temp
for item in stringList:
    print(item, end="")