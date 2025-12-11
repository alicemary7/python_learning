# A company records the energy output (in kWh) from a solar panel for 15 days.
#   An “efficiency drop streak” occurs when three consecutive days show decreasing output.
#   Given the list, determine how many such streaks occur.
# Example: [50, 48, 45, 49, 47, 46, 44]
# Output: 2
# Explanation:
# (Streaks: 50→48→45 and 49→47→46)
# So the count becomes 2 


# def count_streaks(data):
#     count = 0
#     for i in range(len(data) - 2):
#         if data[i] > data[i+1] > data[i+2]:
#             count += 1
#     print(count)
        
# count_streaks([50, 48, 45, 49, 47, 46, 44])   