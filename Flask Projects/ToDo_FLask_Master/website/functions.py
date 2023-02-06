from . import sql_db # ie. from .__init
from .models import Todo
from flask import request


class functions():
    # Returns all list of all toDos
    def get_allTodos():
        allTodoList = Todo.query.all()
        return allTodoList

    # Returns info of ToDo
    def get_info():
        info = {
            'title': request.form['title'],
            'desc': request.form['desc']    
        }
        return info

    # Returns specific toDo obj using filter_by
    def get_todo_by_srno(srNo):
        todo = Todo.query.filter_by(sno=srNo).first() # .first() will return the first row (use this even though sno is primary key)
        return todo

    # DB Operations
    def db_operation(operation, toDo):
        if operation == 'add':
            sql_db.session.add(toDo)
        elif operation == 'delete':
            sql_db.session.delete(toDo)
        sql_db.session.commit()