from typing import List, Dict
from expense import Expense
from income import Income

class BudgetTracker:
    def __init__(self) -> None:
        self.budget_name: str
        self.budget_categories: Dict[str, float] = {}
        self.incomes: List[Income] = []
        self.expenses: List[Expense] = []

    def total_monthly_income(self) -> float:
        total = 0.0
        
        #Calculate total monthly income amount
        for income in self.incomes:
            if income.income_type == "Monthly":
                total += income.amount
            else:
                total += income.amount / 12

        return total

    def total_expenses(self) -> float:
        #Calculate total monthly expense amount
        total = sum(expense.amount for expense in self.expenses)
        return total

    def allowance_remaining(self) -> float:
        #Calculate remaining allowance in the budget
        remainder = self.total_monthly_income() - self.total_expenses()
        return remainder

    def category_spent(self, category: str) -> float:
        #Calculate how much has been spent for a specific category
        spent = sum(expense.amount for expense in self.expenses
                if expense.category.lower() == category.lower())
        return spent
