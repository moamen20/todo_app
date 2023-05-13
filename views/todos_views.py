from typing import List
from flask import jsonify, request, g, Blueprint
from sqlalchemy.orm import Session

import controllers.todo_controller as todo_crud
from services.user_service import get_current_user
from database.db import get_db
from models.user import UserModel
from schemas.todo_schema import TodoSchema, TodoBaseSchema, TodoUpdateSchema, TodoResponseSchema


todo_bp = Blueprint('todo', __name__)

@todo_bp.before_request
def before_request():
    g.db = get_db()

@todo_bp.teardown_request
def teardown_request(exception):
    db = g.pop('db', None)

    if db is not None:
        db.close()

@todo_bp.route('/todos', methods=['GET'])
def get_my_todos_view():
    current_user = get_current_user(request)
    todos = todo_crud.get_user_todos(g.db, current_user)
    return jsonify(todos)

@todo_bp.route('/todos', methods=['POST'])
def add_todo_view():
    current_user = get_current_user(request)
    todo_data = request.get_json()
    todo_crud.add_todo(g.db, current_user, todo_data)
    todos = todo_crud.get_user_todos(g.db, current_user)
    return jsonify(todos)

@todo_bp.route('/todos', methods=['PUT'])
def update_todo_view():
    current_user = get_current_user(request)
    todo_data = request.get_json()
    todo_crud.update_todo(g.db, new_todo=todo_data)
    todos = todo_crud.get_user_todos(g.db, current_user)
    return jsonify(todos)

@todo_bp.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo_view(todo_id):
    current_user = get_current_user(request)
    todo_crud.delete_todo(g.db, todo_id)
    todos = todo_crud.get_user_todos(g.db, current_user)
    return jsonify(todos)

