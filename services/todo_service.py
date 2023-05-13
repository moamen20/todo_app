from typing import List

from sqlalchemy.orm import Session

from models.todos import TodoModel
from models.user import  UserModel
from schemas.todo_schema import TodoSchema, TodoUpdateSchema


def add_todo(db: Session,current_user: UserModel,todo_data: TodoSchema,) -> TodoModel:
    todo = TodoModel(
        text=todo_data.text,
        completed=todo_data.completed,
    )
    todo.owner = current_user
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo


def update_todo(db: Session,new_todo: TodoUpdateSchema,) -> TodoModel:
    todo = db.query(TodoModel).filter(TodoModel.id == new_todo.id,).first()
    if not todo:
        raise ValueError(f"Todo with ID: {new_todo.id} not found.")
    todo.text = new_todo.text
    todo.completed = new_todo.completed
    db.commit()
    db.refresh(todo)
    return todo


def delete_todo(  db: Session, todo_id: int,):
    todo = db.query(TodoModel).filter(TodoModel.id == todo_id).first()
    if not todo:
        raise ValueError(f"Todo with ID: {todo_id} not found.")
    db.delete(todo)
    db.commit()


def get_user_todos( db: Session,current_user: UserModel,) -> List[TodoModel]:
    todos = db.query(TodoModel).filter(TodoModel.owner == current_user).all()
    return todos
