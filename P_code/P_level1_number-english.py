s="123"

number = ["zero","one","two","three","four","five", "six","seven","eight","nine"]
answer = ""
temp = ""
for item in s:
    if(48<=ord(item) and ord(item)<=57):
        answer+= item
    else:
        temp += item
        for i in range(0,10):
            if(temp == number[i]):
                answer+=str(i)
                temp=""
answer = int(answer)