# FastAPI Learning Journey

Hi, I'm Suryansh — a CS undergrad learning backend development from scratch.
This repo documents my progress day by day as I build real things and push working code.

---

## What I've Built So Far

### Day 1 — FastAPI Basics
My first ever API endpoints. Learned how the web works, what HTTP methods are,
and how FastAPI makes it simple to build APIs in Python.

**What I learned:**
- GET requests and returning data
- Path parameters ( /product/{id} )
- POST requests with Pydantic validation
- FastAPI auto documentation at /docs

### Day 2 — Real Database with MySQL
Connected the API to an actual MySQL database.
No more fake/hardcoded data — everything now saves and loads from DB.

**What I learned:**
- Connecting FastAPI to MySQL using SQLAlchemy
- Defining database tables as Python classes (models)
- Full CRUD — Create, Read, Delete products
- How database sessions work per request

### Day 3 — Authentication with JWT
Added real login and signup. Passwords are hashed before saving to database.
All product routes are now protected — you must login first to access them.

**What I learned:**
- Password hashing with Bcrypt
- Creating and verifying JWT tokens
- Protecting routes with HTTPBearer
- Register and Login endpoints
- Dependency injection in FastAPI

---

## How to Run

```bash
git clone https://github.com/suryansh173/FastAPI-Learning.git
cd FastAPI-Learning

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

cd day2-database
uvicorn main:app --reload
```

Open http://127.0.0.1:8000/docs to test all endpoints interactively.

---

## Stack
Python, FastAPI, MySQL, SQLAlchemy, Pydantic

---

*More days coming — authentication, React frontend, and deployment next.*