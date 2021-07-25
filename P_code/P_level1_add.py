absolutes = [4,7,12]
signs = [True, False, True]

answer = 0
answer = sum(pair[0] if pair[1] else -1*pair[0] for pair in zip(absolutes, signs))
print(answer)

answer = 0
for i in range(0, len(absolutes)):
    if(signs[i]==False):
        absolutes[i] = -1*absolutes[i]
    answer+= absolutes[i]
print(answer)