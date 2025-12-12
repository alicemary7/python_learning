# A company keeps two lists:

# One list has employee names.

# Another list has each employee’s shift hours (integer).

# A new project needs employees whose shift hours are strictly between two given limits (lower < hours < upper).
# Your task: return a new list of names that match this rule.
# If no employee qualifies or either list is empty, return ["None"].

# Input:
# names = ["Arun", "Beema", "Chandru", "Dev", "Esha"]
# hours = [5, 9, 12, 4, 10]
# lower = 6
# upper = 11


def employee_filter(names, hours, lower, upper):
    result = []
    if len(names) == 0 or len(hours) == 0:
        return ["None"]
    for i in range(len(hours)):
        if lower < hours[i] < upper:
            result.append(names[i])
    if len(result) == 0:
        return ["None"]
    return result
names = ["Arun", "Beema", "Chandru", "Dev", "Esha"]
hours = [5, 9, 12, 4, 10]
lower = 6
upper = 11
print(employee_filter(names, hours, lower, upper)) 