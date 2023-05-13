import os
from typing import List

from flask import Blueprint, jsonify, request
from sqlalchemy.orm import Session


import controllers.user_controller as user_crud
from database.db import get_db
from models.user import UserModel

from schemas.user_schema import UserSchema, UserCreateSchema

user_bp = Blueprint('user', __name__)

@user_bp.route("/users")
def users():
    with get_db() as db:
        users = user_crud.get_all_users(db)
        return jsonify(list(users))

@user_bp.route("/users/<email>")
def get_user(email: str):
    with get_db() as db:
        user = user_crud.get_user_by_email(db, email)
        if user:
            return jsonify(user)
        else:
            return jsonify({'message': 'user not found'}), 404

@user_bp.route("/users", methods=["POST"])
def sign_up():
    user_data = request.get_json()
    with get_db() as db:
        user = user_crud.get_user_by_email(db, user_data['email'])
        if user:
            return jsonify({'detail': 'email exist'}), 409
        new_user = user_crud.add_user(db, user_data)
        return jsonify(new_user)


@user_bp.route("/users/login", methods=["POST"])
def login():
    user_data = request.get_json()
    with get_db() as db:
        user = user_crud.get_user_by_email(db, user_data['email'])
        if not user or user.password != user_data['password']:
            return jsonify({'message': 'Invalid email or password'}), 401
        return jsonify({'message': 'Login successful'})
