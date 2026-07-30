from dataclasses import dataclass

@dataclass
class Expense:
    category: str
    amount: float
    recurring: bool #Monthly recurrence
