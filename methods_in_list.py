# pop() By index (or last item), returns the removed item.


n=['a,','b','c','d']
n.pop(3)
print(n)

# remove() By value, no return.

n=['a,','b','c','d']
n.remove('b')
print(n)

# del[]  By index or slice, no return, can delete variables

n=['a,','b','c','d']
del n[0]
print(n)

# Spili()

sentence = "Python is a powerful language"
words = sentence.split()
print(words)

# spilitting value in string using index value

text = "one-two-three-four"
parts = text.split("-", 2)
print(parts)

# append()
t1 = ['a', 'b', 'c']
t1.append(['d', 'e'])
print(t1)

t1 = ['a', 'b', 'c']
t2=['d', 'e']
t1.append(t2)
print(t1)



# extend()
t1 = ['a', 'b', 'c']
t1.extend(['d', 'e'])
print(t1)

t1 = ['a', 'b', 'c']
t2=['d', 'e']
t1.extend(t2)
print(t1)

# sort()
cars = ['Ford', 'BMW', 'Volvo']

cars.sort(reverse=True)

print(cars)

# min and max()

min_val = min(10, 5, 20, 15, 8)
max_val = max(10, 5, 20, 15, 8)
print(f"Minimum value: {min_val}")  
print(f"Maximum value: {max_val}")