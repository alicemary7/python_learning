# Rotate a list to the right by 1 step (no slicing)
# Input: [1,2,3,4,5]
#  Output: [5,1,2,3,4]


def last_ele_at_first(nums):
    result=[]
    for i in range(-1,len(nums)-1,+1):
        result.append(nums[i])
last_ele_at_first([1,2,3,4,15])



n=[1,2,3,4,5]
res=[]
a=n[-1]
res.append(a)
res.extend(n[0:len(n)-1])
print(res)