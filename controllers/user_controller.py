import os
from typing import Optional, List
from flask import Blueprint, jsonify, request
from sqlalchemy.orm import Session
from werkzeug.exceptions import BadRequest, NotFound

from database.db import get_db
from models import UserModel
from schemas.user_schema import UserSchema, UserCreateSchema
from services.user_service import add_user, get_all_users, get_user_by_email

auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/users/", methods=["GET"])
def read_users(skip: int = 0, limit: int = 100):
    with get_db() as db:
        users = get_all_users(db)
        return jsonify(users)


@auth_bp.route("/users/", methods=["POST"])
def create_user():
    try:
        user_data = request.get_json()
        user = UserCreateSchema(**user_data)
    except (TypeError, ValueError) as e:
        raise BadRequest(str(e))

    with get_db() as db:
        db_user = get_user_by_email(db, email=user.email)
        if db_user:
            raise BadRequest("Email already registered")
        new_user = add_user(db=db, user_data=user)
        return jsonify(UserSchema.from_orm(new_user))


@auth_bp.route("/users/<int:user_id>", methods=["GET"])
def read_user(user_id: int):
    with get_db() as db:
        user = db.query(UserModel).filter_by(id=user_id).first()
        if not user:
            raise NotFound("User not found")
        return jsonify(UserSchema.from_orm(user))


@auth_bp.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id: int):
    try:
        user_data = request.get_json()
        user = UserCreateSchema(**user_data)
    except (TypeError, ValueError) as e:
        raise BadRequest(str(e))

    with get_db() as db:
        db_user = db.query(UserModel).filter_by(id=user_id).first()
        if not db_user:
            raise NotFound("User not found")
        db_user.update(user_data)
        db.commit()
        return jsonify(UserSchema.from_orm(db_user))


@auth_bp.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id: int):
    with get_db() as db:
        user = db.query(UserModel).filter_by(id=user_id).first()
        if not user:
            raise NotFound("User not found")
        db.delete(user)
        db.commit()
        return "", 204

