habits = ("Exercise", "Read Books", "Meditation", "Drink Water")
weekly_completion = (1, 1, 0, 1, 1, 0, 1)

print("--- Habit Tracker Details ---")

total_habits = len(habits)
tracked_days = len(weekly_completion)
print("Number of habits tracked:", total_habits)
print("Number of days recorded:", tracked_days)

first_habit = habits[0]
print("My first habit is:", first_habit)

weekday_records = weekly_completion[0:5]
print("Weekday completion records:", weekday_records)

print("\n--- Testing Immutability ---")
try:
    habits[0] = "Running"
except TypeError as error:
    print("Cannot change tuple directly:", error)
    print("Explanation: Tuples are immutable, meaning they cannot be modified after creation.")