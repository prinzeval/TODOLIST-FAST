This project is a simple Todo List application that demonstrates basic CRUD (Create, Read, Update, Delete) operations. 
The application is built using FastAPI for the backend and SQLite for the database. The frontend is created with HTML and CSS.

Features
Create: Add new todo items.
Read: Display all todo items.
Update: Mark todo items as complete or incomplete.
Delete: Remove todo items.
Technologies Used
Backend: FastAPI
Database: SQLite
Frontend: HTML, CSS
Getting Started
Prerequisites
Python 3.7+
Pip

pip install fastapi

pip install "uvicorn[standard]"

pip install python-multipart sqlalchemy jinja2


uvicorn app:app --reload
