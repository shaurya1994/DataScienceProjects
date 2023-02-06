Steps to reproduce

SQLite operations on VS code (SQLite extension required)
ctrl+shift+p > SQLite: Open Database > Select created DB

To run project
in terminal
>> flask run

in terminal for creating db (OPTIONAL: If db is not created automatically)
>> python
>> from app import db
>> db.create_all()
