nums = [1,2,3,4,5,6]

answer = min(len(nums)//2, len(list(set(nums))))
print(answer)