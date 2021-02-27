import sys
T = int(sys.stdin.readline())
member_list =[]
for _ in range(T):
    age, name = map(str,sys.stdin.readline().split())
    member_list.append((int(age),name))
member_list.sort(key=lambda list:int(list[0]))
for i in range(len(member_list)):
    print(str(member_list[i][0])+" "+member_list[i][1])