strings = ["abce","abcd","cdx"]
n = 2

print(sorted(strings, key=lambda x:(x[n],x)))