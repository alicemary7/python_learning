# ages → age of each student

# scores → exam score of each student

# You must return a NEW list of students who satisfy all 3 conditions, using only ONE loop:

# Age must be 18 or above

# Score must be at least 75

# Both lists must have even index positions (0, 2, 4, …)

# If no student satisfies all conditions, return an empty list.

# ages   = [17, 18, 21, 19, 22, 16]
# scores = [80, 60, 78, 90, 74, 95]


def conditions(age,score):
    new=[]
    for i in range(len(age)):
        if age[i] >= 18 and score[i]>=75 and i%2==0:
            new.append(age[i])
    return new
print(conditions([17, 18, 21, 19, 22, 16],[80, 60, 78, 90, 74, 95]))