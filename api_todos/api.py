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


"""
@app.route("/add_one")
def add_one(request):

    db.todos.insert_one({'title': "todo title", 'body': "todo body"})
    return flask.jsonify(message="success")
    
@app.route('/create-many')
def create_many():
    new_user_1 = {'Name' : 'xyz1', 'Age' : 10}
    new_user_2 = {'Name' : 'xyz2', 'Age' : 20}
    new_user_3 = {'Name' : 'xyz3', 'Age' : 30}
    new_users = [new_user_1, new_user_2, new_user_3]
    db_operations.insert_many(new_users)
    result = {'result' : 'Created successfully'}
    return result
    
    
@app.route('/read')
def read():
    users = db_operations.find()
    output = [{'Name' : user['Name'], 'Age' : user['Age']} for user in users]
    #print(output)
    return jsonify(output)
@app.route("/add_one")
def add_one():
    db.todos.insert_one({'title': "todo title", 'body': "todo body"})
    return flask.jsonify(message="success")
    {
{   "title": "ogle yemegi",
    "description": "oglen yemek yapilacak",
    "is_completed": false,
    "created_date": {
        "$date": "2019-12-31T21:06:00.000Z"
    },
    "updated_date": {
        "$date": "2019-12-30T21:12:00.000Z"
    }
}
}
@"""
