import os
from typing import Union, Optional
from flask import Flask, jsonify, request
from passlib.context import CryptContext
from jose import jwt, JWTError
from database.db import get_db

from controllers import user_controller
from models import UserModel

app = Flask(__name__)

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')



def hash_password(plain_password: str) -> str:
    return pwd_context.hash(plain_password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

