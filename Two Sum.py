nums = list(map(int,input().split()))
target = int(input())
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if target == (nums[i]+nums[j]):
            print(i,j)
            