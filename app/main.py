from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from app import models, schemas, crud, services, dependencies
from app.database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Python Finance System API")

# --- RECORD MANAGEMENT ---

@app.post("/transactions/", response_model=schemas.TransactionResponse)
def create_transaction(
    transaction: schemas.TransactionCreate, 
    db: Session = Depends(get_db),
    role: str = Depends(dependencies.verify_role("Admin")) # Only Admin can create
):
    return crud.create_transaction(db=db, transaction=transaction)

@app.get("/transactions/", response_model=List[schemas.TransactionResponse])
def read_transactions(
    category: Optional[str] = None,
    t_type: Optional[str] = None,
    db: Session = Depends(get_db),
    role: str = Depends(dependencies.verify_role("Viewer")) # Viewers, Analysts, Admins can read
):
    return crud.get_transactions(db, category=category, t_type=t_type)

@app.delete("/transactions/{transaction_id}")
def remove_transaction(
    transaction_id: int, 
    db: Session = Depends(get_db),
    role: str = Depends(dependencies.verify_role("Admin")) # Only Admin can delete
):
    if not crud.delete_transaction(db, transaction_id):
        raise HTTPException(status_code=404, detail="Transaction not found")
    return {"detail": "Transaction deleted successfully"}

# --- ANALYTICS ---

@app.get("/analytics/summary")
def get_finance_summary(
    db: Session = Depends(get_db),
    role: str = Depends(dependencies.verify_role("Analyst")) # Only Analyst or Admin
):
    return services.get_financial_summary(db)

@app.patch("/transactions/{transaction_id}", response_model=schemas.TransactionResponse)
def update_existing_transaction(
    transaction_id: int,
    transaction_update: schemas.TransactionUpdate,
    db: Session = Depends(get_db),
    role: str = Depends(dependencies.verify_role("Admin"))
):
    db_transaction = crud.update_transaction(db, transaction_id, transaction_update)
    if not db_transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return db_transaction