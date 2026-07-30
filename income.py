from dataclasses import dataclass

@dataclass
class Income:
    category: str
    income_type: str #Annualy or Monthly income
    amount: float 
    
