n = 4

#방법 1
answer ="수박"*(n//2)
if(n%2==1):
    answer+="수"
print(answer)

#방법 2
print("수박"*(n//2)+"수"*(n%2))