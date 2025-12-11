# .Print numbers that appear more than once (duplicates only)
# Input: [1,4,2,7,4,1,8,2,2]
#  Output → 1, 2, 4


def remove_repeated(nums):
    result=[]
    count=0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] ==  nums[j]:
                 if nums[i] not in result:
                     result.append(nums[i])
    print(result)

remove_repeated([1,4,2,7,4,1,8,2,2])