num = 9867128
result = []
while num > 0:
    digit = num % 10
    print(digit)
    result.append(digit)
    num //= 10

    
final_result = []
for i in range(len(result)-1, -1, -1):
    final_result.append(result[i])
    print(final_result)
status="unsaturated"
count=0
for i in range(len(final_result)):
    for j in range(i+1, len(final_result)):
        if final_result[i] == final_result[j]:
            count+=1
    if count ==1:
        status="saturated"
print(status)
