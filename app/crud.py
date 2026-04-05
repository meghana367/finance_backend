from sqlalchemy.orm import Session
from app import models, schemas

def get_transactions(db: Session, skip: int = 0, limit: int = 100, category: str = None, t_type: str = None):
    query = db.query(models.Transaction)
    if category:
        query = query.filter(models.Transaction.category == category)
    if t_type:
        query = query.filter(models.Transaction.type == t_type)
    return query.offset(skip).limit(limit).all()

def create_transaction(db: Session, transaction: schemas.TransactionCreate):
    # Convert Pydantic to Dict, then unpack into Model
    data = transaction.model_dump()
    db_transaction = models.Transaction(**data) 
    
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

def delete_transaction(db: Session, transaction_id: int):
    db_transaction = db.query(models.Transaction).filter(models.Transaction.id == transaction_id).first()
    if db_transaction:
        db.delete(db_transaction)
        db.commit()
        return True
    return False

def update_transaction(db: Session, transaction_id: int, transaction_update: schemas.TransactionUpdate):
    db_transaction = db.query(models.Transaction).filter(models.Transaction.id == transaction_id).first()
    if not db_transaction:
        return None
    update_data = transaction_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_transaction, key, value)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction