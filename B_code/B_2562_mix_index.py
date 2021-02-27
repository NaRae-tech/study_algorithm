numL = []
for i in range(0,9):
    n=int(input())
    numL.append(n)
mix = numL[0]
mix_ind = 0
for i in range(1,9):
    if(mix<numL[i]):
        mix = numL[i]
        mix_ind = i
print(mix)
print(mix_ind+1)