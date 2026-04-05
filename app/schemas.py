from pydantic import BaseModel, Field
from datetime import date as dt_date
from typing import Optional
from app.models import TransactionType 

class TransactionBase(BaseModel):
    amount: float = Field(..., gt=0)
    type: TransactionType 
    category: str
    date: Optional[dt_date] = None
    description: Optional[str] = None

class TransactionUpdate(BaseModel):
    amount: Optional[float] = Field(None, gt=0)
    type: Optional[TransactionType] = None
    category: Optional[str] = None
    date: Optional[dt_date] = None
    description: Optional[str] = None

class TransactionCreate(TransactionBase):
    pass

class TransactionResponse(TransactionBase):
    id: int

    class Config:
        from_attributes = True
