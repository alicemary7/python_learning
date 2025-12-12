# Input Example:
team = ['A','B','A','A','B']
score = [50, 90, 80, 60, 70]

# Expected Output:
# B 80.0
s=0
avg=0
count=0
for i in range(len(team)):
    if team[i] =="B":
        s+=score[i]
        count+=1
        avg=s/count
print(avg)