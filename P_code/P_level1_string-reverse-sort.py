s = "Zbcdefg"
s= sorted(s,key=lambda x:-ord(x))
answer =""
for item in s:
    answer+=item
print(answer)