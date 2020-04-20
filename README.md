# AAM Backend part of  Web application
Written in Python ~3.7

Used libraries:
- fastapi and its dependencies
- uvicorn
- SQLAlchemy
- psycopg2
- pyjwt
- passlib

## Installation
```shell script
python -m venv [your_venv_name] # Or use your existing venv
source /path/to/venv/bin/activate
pip install -r requirements

# Specify your own database server credits in app/database.py
python app/migrate.py
```
> In future I will add docker deployment

## Starting Up
```shell script
uvicorn app.main:app --reload
```

## Documentation
Code is documented

API documented automatically and available at [your_host]:[your_port]/redoc
