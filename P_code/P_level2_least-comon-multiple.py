arr = [1,2,3]

arr.sort()
import math
div = arr[-1]
for i in range(len(arr)-2,-1,-1):
    gcd = math.gcd(arr[i],div)
    div = (div*arr[i])//gcd
print(div)