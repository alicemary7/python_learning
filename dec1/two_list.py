# You are given a list of product types ("A" or "B") and a list of sales amounts.
# Calculate which product type has the higher total sales and print the type and its total.

# Input Example:
# product = ['A','B','A','B','A']
# sales = [10, 20, 15, 5, 30]

# Expected Output:
# A 55

product = ['A','B','A','B','A']
sales = [10, 20, 15, 5, 30]
sum=0
for i in range(len(product)):
    if product[i] == "A":
        sum+=sales[i]
print(sum)



# Input Example:
# group = ['Adult','Child','Adult','Adult','Child']
# ages = [34, 12, 45, 29, 8]

# Expected Output:
# Adult 3

group = ['Adult','Child','Adult','Adult','Child']
ages = [34, 12, 45, 29, 8]
m_count=0
count=0
for i in range(len(group)):
    if group[i] == "Child":
        count=count+1
    elif group[i] == "Adult":
        m_count+=1
print(m_count,"->",group[0],",",count,"->",group[1])


