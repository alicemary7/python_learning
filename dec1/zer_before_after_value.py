# zero before and after value

nums = [0, 1, 2, 0, 3, 4, 5, 0, 6, 7]

result = []
zero_count = 0
start = 0
end = 0


for i in range(len(nums)):
    if nums[i] == 0:
            start=nums[i-1]
            end=nums[i+1]
            result.append(start) 
            result.append(end)
            
print(result)