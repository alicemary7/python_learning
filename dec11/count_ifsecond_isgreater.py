# Count pairs where the second number is bigger
# Test case 1:
# Input

# [1, 5, 2, 6, 3, 9]
# Output

# 3
# Test case 2:
# Input

# [10, 9, 8, 7]
# Output

# 0


def second_is_greater(nums):
    count=0
    for i in range(len(nums)-1):
        if nums[i] < nums[i+1]:
            count+=1
    print(count)
second_is_greater([1, 5, 2, 6, 3, 9])