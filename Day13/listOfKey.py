from collections import defaultdict

students = [('A', 90), ('B', 80), ('A', 85), ('B', 88)]
grades = defaultdict(list)

for name, mark in students:
    grades[name].append(mark)

print(dict(grades))
