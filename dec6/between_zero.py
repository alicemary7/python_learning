nums = [0,1, 2, 0, 3, 4, 5, 0, 6, 7]

result = []
start_index = 0
end_index = 0


for i in range(len(nums)):
    if nums[i] == 0:
        start_index = i
        break


for j in range(start_index + 1, len(nums)):
    if nums[j] == 0:
        end_index = j
        break


for k in range(start_index + 1, end_index):
    result.append(nums[k])

print(result)