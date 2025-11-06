students_heights = [156, 178, 165, 171, 187]

total_heights = 0
avg_heights = 0
for h in students_heights:
    total_heights += h
    avg_heights = (total_heights/len(students_heights))

print(f"Average height: {avg_heights}")

print(f"Total height: {total_heights}")

print(f"Total students: {len(students_heights)}")

