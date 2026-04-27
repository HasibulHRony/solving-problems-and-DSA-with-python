#finding good pairs from list

nums = [2, 5, 5, 3, 2, 1, 9, 5]

ans = 0
for i in range(len(nums)):
    count = 0
    for j in range(i+1, len(nums)):
        if nums[i] == nums[j]:
            count +=1
    ans = count + ans

print(ans)  