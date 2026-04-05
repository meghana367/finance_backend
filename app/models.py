import enum
import datetime
from sqlalchemy import Column, Integer, Float, String, Date, Enum
from app.database import Base

class TransactionType(enum.Enum):
    income = "income"  # Use lowercase to match JSON standard
    expense = "expense"

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    # Adding name="transaction_type" helps SQLite handle the Enum
    type = Column(Enum(TransactionType, name="transaction_type"), nullable=False)
    category = Column(String, index=True)
    date = Column(Date, default=datetime.date.today)
    description = Column(String, nullable=True)