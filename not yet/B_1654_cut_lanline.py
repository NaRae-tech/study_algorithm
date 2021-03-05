result = []
def howmanymake(lenline, length):
    count =0
    for i in range(0,len(lenline)):
        count+=(lenline[i]//length)
    return count
def howlong(lenline, left,right, mid,N):
    makeit = howmanymake(lenline,mid)
    if(makeit>N):
        if(left==mid or right==mid):
            return
        return howlong(lenline, mid, right, (mid+right)//2,N)
    elif(makeit<N):
        if (left == mid or right == mid):
            return
        return howlong(lenline,left,mid,(left+mid)//2,N)
    elif(makeit==N):
        result.append(mid)
        temp = mid
        while(True):
            temp+=1
            if(howmanymake(lenline, temp) == N):
                result.append(temp)
            else:
                break
        temp = mid
        while (True):
            temp-=1
            if(howmanymake(lenline, temp) == N):
                result.append(temp)
            else:
                break
import sys
K,N=map(int,sys.stdin.readline().split())
lenline= []
for _ in range(K):
    lenline.append(int(sys.stdin.readline()))
lenline=sorted(lenline)
howlong(lenline,1,lenline[0],(1+lenline[0])//2, N)
result = sorted(result)
print(result[-1])