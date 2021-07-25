n=125

#방법1
a = ""
while(n!=0):
    a+=str(n%3)
    n=n//3
print(int(a,3))

#방법2
#3진법으로 바꾸기
temp =[]
while(n!=0):
    temp.insert(0,n%3)
    n=n//3
print(temp)
#3진법 뒤집기 -> 10진법으로 변환
temp.reverse()
t =""
for item in temp:
    t += str(item)
print(int(t,3))

