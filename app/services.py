from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models import Transaction, TransactionType

def get_financial_summary(db: Session):
    total_income = db.query(func.sum(Transaction.amount)).filter(
        Transaction.type == TransactionType.income
    ).scalar() or 0.0

    total_expenses = db.query(func.sum(Transaction.amount)).filter(
        Transaction.type == TransactionType.expense
    ).scalar() or 0.0

    category_totals = db.query(
        Transaction.category, 
        func.sum(Transaction.amount)
    ).group_by(Transaction.category).all()

    return {
        "total_income": total_income,
        "total_expenses": total_expenses,
        "current_balance": total_income - total_expenses,
        "category_breakdown": {cat: amt for cat, amt in category_totals}
    }
