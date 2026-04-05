# Python Finance System Backend (Internship Assignment)

A modular FastAPI backend designed to manage personal financial records with built-in analytics and role-based security.

## ✨ Core Functionalities

- **Full CRUD:** Create, Read, Update, and Delete financial transactions.
- **Advanced Filtering:** Filter records by category or transaction type (income/expense).
- **Financial Analytics:** Real-time calculation of total income, expenses, and current balance.
- **Role-Based Access Control (RBAC):** Simulated security layers using request headers.
- **Data Integrity:** Strict input validation using Pydantic and SQLAlchemy Enums.

## 🛠️ Tech Stack

- **Framework:** FastAPI
- **Database:** SQLite (SQLAlchemy ORM)
- **Validation:** Pydantic v2
- **Server:** Uvicorn

## 🚦 Getting Started

1. **Activate Environment:** `.\venv\Scripts\activate`
2. **Install Dependencies:** `pip install -r requirements.txt`
3. **Run Application:** `python -m uvicorn app.main:app --reload`
4. **Interactive Docs:** Visit `http://127.0.0.1:8000/docs`

## 🔐 Security & Roles

The system simulates authentication via the `x-user-role` header:

- **Admin:** Full access (Create, Update, Delete, View).
- **Analyst:** Access to the `/analytics/summary` and View-only transactions.
- **Viewer:** Restricted to `GET /transactions/` only.

## 💡 Assumptions

- Calculations assume a single currency for all entries.
- The `x-user-role` header is used to demonstrate RBAC logic without the overhead of a full JWT implementation.
