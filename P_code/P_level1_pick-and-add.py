numbers = [0,1,2,3,100,1123]

import itertools
pick = list(itertools.combinations(numbers,2))
print(pick)
answer = []
for i in range(0, len(pick)):
    answer.append(pick[i][0]+pick[i][1])
print(sorted(list(set(answer))))