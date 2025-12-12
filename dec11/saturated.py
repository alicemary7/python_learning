num = 986705
result = []
while num > 0:
    digit = num % 10
    result.append(digit)
    num //= 10
    
final_result = []
for i in range(len(result)-1, -1, -1):
    final_result.append(result[i])
status="saturated"
for i in range(len(final_result)):
    for j in range(i+1, len(final_result)):
        if final_result[i] == final_result[j]:
            status = "unsaturated"
            break
print(status)