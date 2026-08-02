from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(200), nullable=False)
    email = Column(String(200), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    monthly_budgets = relationship(
        "MonthlyBudget",
        back_populates="user",
        cascade="all, delete-orphan",
    )


class MonthlyBudget(Base):
    __tablename__ = "monthly_budgets"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    year = Column(Integer, nullable=False)
    month = Column(String(100), nullable=False)
    total_amount = Column(Numeric(10, 2), nullable=False)

    user = relationship("User", back_populates="monthly_budgets")
    budget_items = relationship(
        "BudgetItem",
        back_populates="monthly_budget",
        cascade="all, delete-orphan",
    )


class BudgetItem(Base):
    __tablename__ = "budget_items"

    id = Column(Integer, primary_key=True, index=True)
    budget_id = Column(Integer, ForeignKey("monthly_budgets.id"), nullable=False)
    name = Column(String(200), nullable=False)
    percentage = Column(Numeric(5, 2), nullable=False)
    parent_id = Column(Integer, nullable=True)

    monthly_budget = relationship("MonthlyBudget", back_populates="budget_items")

