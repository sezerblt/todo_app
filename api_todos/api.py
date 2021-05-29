import datetime
import time
from flask import Flask, render_template, request, url_for, redirect
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)
app.config["MONGO_URI"] = 'mongodb://localhost:27017/localDB'
mongo = PyMongo(app)


todos = mongo.db.todos

@app.route('/')
def index():
    saved_todos = todos.find()
    return render_template('index.html', todos=saved_todos)

@app.route('/add', methods=['POST'])
def add_todo():
    new_title        = request.form.get('new-title')
    new_description  = request.form.get('new-description')
    new_create_date         = request.form.get('new-create-date')
    new_update_date  = request.form.get('new-update-date')
    new_is_completed = request.form.get('new-is-completed')
    context={
        'title': new_title,
        'description': new_description,
        'is_completed': False,
        'created_date':new_create_date,
        'updated_date':new_update_date
    }
    todos.insert_one(context)
    return redirect(url_for('index'))

@app.route('/complete/<oid>')
def complete(oid):
    todo_item = todos.find_one({'_id': ObjectId(oid)})
    todo_item['is_completed'] = True
    todos.save(todo_item)
    return redirect(url_for('index'))

@app.route('/delete_completed')
def delete_completed():
    todos.delete_many({'is_completed' : True})
    return redirect(url_for('index'))

@app.route('/delete_all')
def delete_all():
    todos.delete_many({})
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True)

