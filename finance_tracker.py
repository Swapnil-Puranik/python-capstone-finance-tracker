# Capstone Project for Python Externship
print("Welcome to the Personal Finance Tracker!")

def add_expense(data):
    try:

        category = input("Enter category: ").strip()
        if not category:
            raise ValueError("Category cannot be empty.")

        description = input("Enter expense description: ").strip()
        if not description:
            raise ValueError("Description cannot be empty.")

        amt = input("Enter amount: ").strip()
        amount = float(amt)
        if amount < 0: # No negative amount allowed
            raise ValueError("Amount cannot be negative.")

        expense = (description, amount)
        if category in data:
            data[category].append(expense) # If the category exists, we add the new expense to the list
        else:
            data[category] = [expense] # Adding list of tuples, so we can append to it and take sum

        print("Expense added successfully.")
    except ValueError:
        print("Invalid input, please enter a valid number")
    except Exception:
        print("Oops! Something went wrong! Try Again")

def view_expenses(data):
    if not data:
        print("No expenses to show.")
        return
    for category, expenses in data.items():
        print(f"\nCategory: {category}")
        for desc, amt in expenses:
            print(f"  - {desc}: ${amt:.2f}") # show amount up till 2 decimal places

def view_summary(data):
    if not data:
        print("No expenses to summarize.")
        return

    print("\nSummary:")
    for category, expenses in data.items():
        total = sum(amount for desc, amount in expenses)
        print(f"{category}: ${total:.2f}")

expenses_data = {}
while True:

    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Summary")
    print("4. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        add_expense(expenses_data)
        print("-"*40)
    elif choice == "2":
        view_expenses(expenses_data)
        print("-" * 40)
    elif choice == "3":
        view_summary(expenses_data)
        print("-" * 40)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")

