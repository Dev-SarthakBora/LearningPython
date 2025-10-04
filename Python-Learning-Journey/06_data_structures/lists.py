# lists.py
import random

data = [random.randint(1, 100) for _ in range(20)]
filtered = [x for x in data if x % 3 == 0 and x > 30]
grouped = [data[i:i+5] for i in range(0, len(data), 5)]
flattened = [x for group in grouped for x in group]
averages = [sum(chunk)/len(chunk) for chunk in grouped]
sorted_unique = sorted(set(data))
rotated = data[-3:] + data[:-3]
print(data)
print(filtered)
print(grouped)
print(flattened)
print(averages)
print(sorted_unique)
print(rotated)

