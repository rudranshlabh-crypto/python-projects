grade_book = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 95,
    "Ethan": 88
}

total_score = 0
for score in grade_book.values():
    total_score += score

class_average = total_score / len(grade_book)
print(f"Class Average: {class_average:.2f}")

top_student = max(grade_book, key=grade_book.get)
bottom_student = min(grade_book, key=grade_book.get)

print(f"Top Scorer: {top_student} with a score of {grade_book[top_student]}")
print(f"Bottom Scorer: {bottom_student} with a score of {grade_book[bottom_student]}")

search_name = input("\nEnter the student name to look up: ")
student_grade = grade_book.get(search_name, None)

if student_grade is not None:
    print(f"{search_name}'s score is: {student_grade}")
else:
    print(f"Sorry, '{search_name}' is not in the grade book. Please check the spelling.")