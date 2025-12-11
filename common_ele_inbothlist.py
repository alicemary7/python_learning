# Find the common elements between two lists A and B.
#  Return a new list containing only the elements that appear in both lists,
#  in the same order as they appear in A.
# TEST CASE 1
# Input:

# A = [1, 2, 3, 4]
# B = [3, 4, 5, 6]
# Output:

# [3, 4]
# Test Case 2
# Input:

# A = [10, 20, 30, 40]
# B = [50, 60, 70]
# Output:

# []

def common_elements(a,b):
    result=[]
    for i in range(len(a)):
        if a[i] in  b:
            result.append(a[i])
    print(result)
common_elements([10, 20, 30, 40],[50,40, 60, 70])