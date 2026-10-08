# Library Manager (Django + SQLite)

A Django website for managing books, members and borrowings. Data is stored
in SQLite using Django Models and the ORM.

## Setup

```
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open http://127.0.0.1:8000/ (admin: http://127.0.0.1:8000/admin/)