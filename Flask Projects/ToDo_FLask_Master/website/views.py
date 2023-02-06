import json
from .models import Todo
from .functions import functions
from flask import Blueprint, request, redirect, render_template


# Stores the standard routes for the website and also for rendering custom templates
views = Blueprint('views', __name__)

# ROUTES
# 'GET', 'POST' are the methods allowed on the URL
@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method=='POST':
        to_do_info = functions.get_info()
        to_do = Todo(title=to_do_info['title'], desc=to_do_info['desc'])
        functions.db_operation(operation='add', toDo=to_do)
        
    return render_template('index.html', allTodo=functions.get_allTodos()) # *Important (Passing allTodo to specific .html file)


# ShowAll ToDos
@views.route('/show-all', methods=['GET'])
def showAll_todos():
    return render_template('showAll.html', allTodo=functions.get_allTodos()) 


# About Project
@views.route('/about-project')
def about_project():
    json_file = 'website/static/data/about.json' 
    # data_dict = json.load(json_file)  # Causes error if file is empty
    
    with open(json_file, 'r') as j:
        data_dict = json.loads(j.read())
    
    return render_template('aboutProject.html', data=data_dict)    


# Update ToDo
@views.route('/update/<int:srNo>', methods=['GET', 'POST']) # *Important Params passed here <int:srNo> is passed in 'def update(srNo)'
def update(srNo):
    if request.method=='POST': # If the ToDo is updated

        to_do = functions.get_todo_by_srno(srNo)
        to_do_info = functions.get_info() # To get values from the form
        
        to_do.title = to_do_info['title'] 
        to_do.desc = to_do_info['desc']
        
        functions.db_operation(operation='add', toDo=to_do)
        return redirect('/')
        
    to_do = functions.get_todo_by_srno(srNo)
    return render_template('update.html', todo=to_do)


# Delete ToDo
@views.route('/delete/<int:srNo>', methods=['GET'])
def delete(srNo):
    to_do = functions.get_todo_by_srno(srNo)
    functions.db_operation(operation='delete', toDo=to_do)
    # return redirect('/')
    return redirect(request.referrer)