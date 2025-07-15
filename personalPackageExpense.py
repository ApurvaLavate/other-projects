import csv
import os
from datetime import datetime

FILENAME = "expenses.csv"

def initialize_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description"])

# Add a new expense
def add_expense():
    date = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")

    category = input("Enter category (e.g. Food, Transport, etc.): ")
    amount = input("Enter amount: ")
    description = input("Enter description (optional): ")

    with open(FILENAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])
    
    print("Expense added successfully!")

def view_expenses():
    with open(FILENAME, mode="r") as file:
        reader = csv.reader(file)
        next(reader)  
        print("\n=== All Expenses ===")
        for row in reader:
            print(f"{row[0]} | {row[1]} | ₹{row[2]} | {row[3]}")

def delete_expense():
    view_expenses()
    line_number = int(input("Enter the expense number to delete: "))

    with open(FILENAME, mode="r") as file:
        lines = list(csv.reader(file))

    if 0 < line_number < len(lines):
        removed = lines.pop(line_number)
        with open(FILENAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(lines)
        print(f"Deleted expense: {removed}")
    else:
        print("Invalid entry.")

def show_summary():
    totals = {}
    with open(FILENAME, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            category = row["Category"]
            amount = float(row["Amount"])
            totals[category] = totals.get(category, 0) + amount

    print("\n=== Expense Summary by Category ===")
    for category, total in totals.items():
        print(f"{category}: ₹{total:.2f}")

def main():
    initialize_file()
    while True:
        print("\n==== PERSONAL EXPENSE TRACKER ====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Show Summary by Category")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            show_summary()
        elif choice == "5":
            print("👋 Exiting. Thank you!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
