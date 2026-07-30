from income import Income
from expense import Expense
from budget_tracker import BudgetTracker

from typing import Dict

def print_line() -> None:
    print("-" * 50)

def create_budget(app: BudgetTracker) -> None:
    print("\nCreate a New Budget")
    print_line()
    print("To create a new budget, start adding a limit for however many categories you need")
    print("Type Homepage at any moment to Return to the Homepage")
    print_line()

    budget_name = input("Enter a name for this budget: ")

    if budget_name == "":
        print("Creation canceled: Returning to Main Menu")
        return

    new_categories: Dict[str, float] = {}

    while True:
        category = input("Enter a category name: ")

        if category == "":
            print("Creation canceled: Returning to Main Menu")
            return

        limit = float(input("Enter the limit for this category: "))

        if limit == "":
                print("Creation canceled: Returning to Main Menu")
                return

        new_categories[category] = limit

        print(f"\nCategory Added: {category}")
        print_line()

        print("Type 1 to Add Another Category")
        print("Type 2 to Save Budget")
        print("Type 3 to Cancel without saving")
      
        choice = input("Enter Choice: ")

        if choice == "1":
            continue
        elif choice == "2":
            app.budget_name = budget_name
            app.budget_categories = new_categories

            print("Budget Saved Successfully!")
            input("\nPress Enter to Continue")
            return
        elif choice == "3":
            return

def add_income(app: BudgetTracker) -> None:
    print("Add Income Information")
    print_line()
    print("\nTo add your income information, name a category and enter the amount")
    print("Type Homepage at any moment to Return to the Homepage")
    print_line()

    while True:
        category = input("Enter the Category for the income: ").strip()

        if category.lower() == "homepage" or category == "":
            print("Entry Canceled: Returning to Main Menu")
            return

        print("Type 1 to enter a monthly income")
        print("Type 2 to enter a yearly income")
        print_line()
        choice = input("Enter Choice: ").strip()

        if choice == "1":
            income_type = "Monthly"
        elif choice == "2":
            income_type = "Yearly"
        else:
             print("Invalid Choice: Try Again")
             continue

        try:
            amount = float(input("Enter the income amount: ").strip())

            if amount <= 0:
                print("Invalid Amount: Please enter a positive number")
                continue

        except ValueError:
            print("Invalid Amount: Please enter a positive number")
            print("Examples: 7500 or 2500.55")
            continue

        print("Type 1 to Save your Income")
        print("Type 2 to Cancel without saving")

        choice = input("Enter Choice: ").strip()

        if choice == "1":
            app.incomes.append(Income(category, income_type, amount))
            print("Income Saved Successfully!")
            input("\nPress Enter to Continue")
            return
        elif choice == "2":
            return
        else:
            print("Invalid Choice: Try Again")
            continue      

def add_expense(app: BudgetTracker) -> None:
    print("\nAdd a New Expense")
    print_line()
    print("To add a new expense, start adding expenses the for however many categories you need")
    print("these will be used to calculate your remaining budget")
    print("Type Homepage at any moment to Return to the Homepage")
    print_line()

    while True:
        print("Choose an Expense Category:")
        print("1. Housing")
        print("2. Food")
        print("3. Transportation")
        print("4. Entertainment")
        print("OR type a custom category name")

        choice = input("Enter Choice: ").strip()

        if choice.lower() == "homepage" or choice == "":
            print("Entry Canceled: Returning to Main Menu")
            return

        if choice == "1":
            category = "Housing"
        elif choice == "2":
            category = "Food"
        elif choice == "3":
            category = "Transportation"
        elif choice == "4":
            category = "Entertainment"
        else:
            category = choice

        try:
            amount = float(input("Enter the expense amount: ").strip())
       
            if amount <= 0:
                print("Invalid Amount: Please enter a positive number")
                continue
       
        except ValueError:
            print("Invalid Amount: Please enter a positive number")
            print("Examples: 150 or 250.55")
            continue

        recurring = input("Is this a recurring expense? Type y or n: ").strip().lower()

        if recurring == "y":
            recurring = True
        elif recurring == "n":
            recurring = False
        else:
            print("Invalid Choice: Please type either y or n")
            continue

        print("Type 1 to Review and Save Expense")
        print("Type 2 to Cancel without saving")

        choice = input("Enter Choice: ").strip()

        if choice == "1":
            print("Are you sure you want to save this expense?")
            print(f"Category: {category}")
            print(f"Amount: ${amount}")
            print(f"Recurring: {'Yes' if recurring else 'No'}")
            print_line()
            print("Type 1 to Save Expense")
            print("Type 2 to re-enter Expense")
            print("Type 3 to Cancel without saving")
            choice = input("Enter Choice: ").strip()

            if choice == "1":
                app.expenses.append(Expense(category, amount, recurring))
                print("Expense Saved Successfully!")
                input("\nPress Enter to Continue")
                return

            elif choice == "2":
                continue

            elif choice == "3":
                print("Entry Canceled: Returning to Main Menu")
                return

        if choice == "2":
            return

def homepage(app: BudgetTracker) -> None:
    while True:
        print("Best Budgeting Tool")
        print_line()
        print("This tool will help you keep track your budget, income, expenses, and remaining allowance!")
        print_line()
        print("Type 1 to navigate to the Main Menu")
        print("Type 2 to Exit the program")
        print_line()

        choice = int(input("Enter Choice: ").strip())

        if choice == 1:
            main_menu(app)
        elif choice == 2:
            exit()
        else:
            print("Invalid Choice: Try Again")

        
def main_menu(app: BudgetTracker) -> None:
    while True:
        print("\nMain Menu")
        print_line()
        print("Type 1 to Create a New Budget")
        print("Type 2 to Add your Income Information")
        print("Type 3 to Add a new Expense")
        print("Type 4 to Return to the Homepage")
        print("Type 5 to Exit the Program")
        print_line()

        choice = int(input("Enter Choice: ").strip())

        if choice == 1:
            create_budget(app)
        elif choice == 2:
            add_income(app)
        elif choice == 3:
            add_expense(app)
        elif choice == 4:
            return
        elif choice == 5:
            exit()
        else:
            print("Invalid Choice: Try Again")


def main():
    app = BudgetTracker()

    try:
        homepage(app)
    except KeyboardInterrupt:
        print("\nProgram Closed: See you next time!")

if __name__ =="__main__":
    main()
