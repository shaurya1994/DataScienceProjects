from . import sql_db # Importing db from __init__.py
from datetime import datetime

class Todo(sql_db.Model):
    # Creating database variables 
    sno = sql_db.Column(sql_db.Integer, primary_key=True)
    title = sql_db.Column(sql_db.String(200), nullable=False)
    desc = sql_db.Column(sql_db.String(500), nullable=False)
    date_created = sql_db.Column(sql_db.DateTime, default=datetime.utcnow)