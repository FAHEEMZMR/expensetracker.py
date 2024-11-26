class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self):
        """Add a new expense."""
        date = input("Enter the date (YYYY-MM-DD): ")
        category = input("Enter the category (e.g., Food, Transport, etc.): ")
        amount = input("Enter the amount: ")

        expense = {
            'date': date,
            'category': category,
            'amount': amount
        }
        self.expenses.append(expense)
        print("Expense added successfully!")

    def view_expenses(self):
        """View all recorded expenses."""
        if not self.expenses:
            print("No expenses recorded yet.")
        else:
            print("\n--- Expense List ---")
            for i, expense in enumerate(self.expenses, 1):
                print(f"{i}. Date: {expense['date']}, Category: {expense['category']}, Amount: {expense['amount']}")
            print("--------------------")

    def save_to_file(self, filename="expenses.txt"):
        """Write expenses to a file."""
        try:
            with open(filename, "a") as file:
                for expense in self.expenses:
                    file.write(f"{expense['date']},{expense['category']},{expense['amount']}\n")
            print(f"Expenses saved to {filename} successfully!")
            self.expenses = []
        except Exception as e:
            print(f"Error saving to file: {e}")

def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Save Expenses to File")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            tracker.add_expense()
        elif choice == "2":
            tracker.view_expenses()
        elif choice == "3":
            tracker.save_to_file()
        elif choice == "4":
            print("Exiting the Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
