from pydantic import BaseModel

class monthlyBudget(BaseModel):
    id: int
    year: int
    month: str
    total_amount: float
    
class budgetItem(BaseModel):
    id: int
    name: str
    budget_id: int
    parent_id: int
    percentage: float
    
class User(BaseModel):
    id: int
    username: str
    email: str
    monthlY_budgets: list[monthlyBudget]
    budge_iItems: list[budgetItem]
    