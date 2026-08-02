from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, ConfigDict


class BudgetItemBase(BaseModel):
    name: str
    percentage: float
    parent_id: Optional[int] = None


class BudgetItemCreate(BudgetItemBase):
    budget_id: Optional[int] = None


class BudgetItem(BudgetItemBase):
    id: int
    budget_id: int

    model_config = ConfigDict(from_attributes=True)


class MonthlyBudgetBase(BaseModel):
    year: int
    month: str
    total_amount: float


class MonthlyBudgetCreate(MonthlyBudgetBase):
    pass


class MonthlyBudget(MonthlyBudgetBase):
    id: int
    user_id: int
    budget_items: List[BudgetItem] = []

    model_config = ConfigDict(from_attributes=True)


class UserBase(BaseModel):
    username: str
    email: str


class UserCreate(UserBase):
    senha: str


class User(UserBase):
    id: int
    created_at: datetime
    monthly_budgets: List[MonthlyBudget] = []

    model_config = ConfigDict(from_attributes=True)