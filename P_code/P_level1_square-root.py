n = 121

#방법1
if (n**0.5)%1==0:
    print(int(((n**0.5)+1)**2))
else:
    print(-1)

#방법 1.1
print (int(((n**0.5)+1)**2)) if (n**0.5)%1==0) else print(-1)

import math
#방법 2
print(int(math.pow(math.sqrt(n)+1,2))) if math.sqrt(n) == int(math.sqrt(n)) else print(-1)

#방법 3
if math.sqrt(n) == int(math.sqrt(n)):
    print(int(math.pow(math.sqrt(n)+1,2)))
else:
    print(-1)