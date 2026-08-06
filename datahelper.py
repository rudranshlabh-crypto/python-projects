class DailyDataHelper:
    def __init__(self):
        self.name = "Rudransh"
        self.data_list = ["Math Quiz", "Code Project", "Read Book"]
        print("Welcome, " + self.name + "!")

    def __del__(self):
        print("The program has ended.")

obj = DailyDataHelper()

print("\n--- Listing Your Data ---")
for index, value in enumerate(helper.data_list):
    print("Index:", index, "-", value)