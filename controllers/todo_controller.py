from typing import List

from flask import Blueprint, jsonify, request, abort
from sqlalchemy.orm import Session

from services.todo_service import get_user_todos, add_todo, update_todo, delete_todo
from database.db import get_db
from models import TodoModel, UserModel
from schemas.todo_schema import TodoSchema, TodoUpdateSchema
from services.user_service import get_current_user


router = Blueprint('todos', __name__, url_prefix='/todos')

todos_app = Blueprint('todos', __name__)

@todos_app.route('/todos', methods=['POST'])
def create_todo():
    db = get_db()
    todo_data = request.get_json()
    current_user = get_current_user() # implement this function to get the current user
    todo = add_todo(db, current_user, todo_data)
    return jsonify(todo)

@todos_app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo_handler(todo_id):
    db = get_db()
    todo_data = request.get_json()
    current_user = get_current_user() # implement this function to get the current user
    todo = update_todo(db, todo_id, todo_data)
    if not todo:
        abort(404, description='Todo not found')
    return jsonify(todo)

@todos_app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo_handler(todo_id):
    db = get_db()
    current_user = get_current_user() # implement this function to get the current user
    todo = delete_todo(db, todo_id)
    if not todo:
        abort(404, description='Todo not found')
    return jsonify({'message': f'Todo with ID {todo_id} deleted successfully'})

@todos_app.route('/todos', methods=['GET'])
def get_todos_handler():
    db = get_db()
    current_user = get_current_user() # implement this function to get the current user
    todos = get_user_todos(db, current_user)
    return jsonify(todos)

