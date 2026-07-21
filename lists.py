marks = [85, 92, 95, 67, 89, 50]

total_students=len(marks)

first_mark=[0]
top_three=[1:4]

total_sum=0

for mark in marks:
    total_sum += marks

averege_mark= total_sum / total_students
largest_mark=max(mark)
smallest_mark=min(mark)

print("--- Student Marks List Analyzer Summary ---")
print("Total number of students: " + str(total_students))
print("First student's mark: " + str(first_mark))
print("Slicing example (subset of marks): " + str(top_three))
print("Total marks combined: " + str(total_sum))
print("Average mark: " + str(round(average_mark, 2)))
print("Smallest mark: " + str(smallest_mark))
print("Largest mark: " + str(largest_mark))