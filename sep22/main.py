# Question1

start=0
end=100
while start<=end:
    if start%5==0:
        print(start)
    start=start+1

# Question2

start=1
end=10
x=int(input())
while start<=end:
    print(start*x)
    start=start+1

# Question3

start=1
end=5
sum=0
while start<=end:
    sum=sum+start
    start=start+1
print(sum)