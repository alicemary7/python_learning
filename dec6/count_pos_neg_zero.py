#  Given an array, count how many numbers are positive, negative, and zero.
# Example:
#  Input: -1 2 0 -4 5 0
#  Output:
#  Positive = 2
#  Negative = 2
#  Zero = 2


n= [-4,7,1,9,-2]
count=0
count_zero=0
count_n=0

for el in n:
    if el >= 1:
        count+=1
    elif el == 0:
        count_zero+=1
    else:
        count_n+=1
        
print(count,count_zero,count_n)