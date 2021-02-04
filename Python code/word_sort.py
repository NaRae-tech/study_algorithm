import sys
T = int(sys.stdin.readline())
wList = []
for _ in range(T):
    word = sys.stdin.readline()
    wList.append((word, len(word)))
wList = list(set(wList))
wList.sort(key = lambda word:(word[1],word[0]))
for word in wList:
    print(word[0], end="")