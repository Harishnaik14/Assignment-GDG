import json
import os

DATA_FILE = "expenses.json"
MONTHLY_BUDGET = 10000  # Set your monthly budget here

def load_expenses():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_expenses(expenses):
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=2)

def add_expense():
    amount = float(input("Amount: "))
    category = input("Category: ")
    date = input("Date (YYYY-MM-DD): ")
    description = input("Description: ")
    expense = {
        "amount": amount,
        "category": category,
        "date": date,
        "description": description
    }
    expenses = load_expenses()
    expenses.append(expense)
    save_expenses(expenses)
    print("✅ Expense added!")

def show_total_spent():
    expenses = load_expenses()
    total_spent = sum(e["amount"] for e in expenses)
    print(f"\n💰 Total Spent: ₹{total_spent:.2f}")

def show_remaining_amount():
    expenses = load_expenses()
    total_spent = sum(e["amount"] for e in expenses)
    remaining = MONTHLY_BUDGET - total_spent
    print(f"\n🧾 Remaining Budget: ₹{remaining:.2f}")

def monthly_summary():
    expenses = load_expenses()
    summary = {}
    for e in expenses:
        month = e["date"][:7]  # Extract YYYY-MM
        summary.setdefault(month, 0)
        summary[month] += e["amount"]
    print("\n📅 Monthly Summary:")
    for month, total in summary.items():
        remaining = MONTHLY_BUDGET - total
        print(f"{month}: Spent ₹{total:.2f}, Remaining ₹{remaining:.2f}")

def main():
    while True:
        print("\n📊 Expense Tracker")
        print("1. Add Expense")
        print("2. Show Total Spent")
        print("3. Show Remaining Amount")
        print("4. Monthly Summary")
        print("5. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            show_total_spent()
        elif choice == "3":
            show_remaining_amount()
        elif choice == "4":
            monthly_summary()
        elif choice == "5":
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()