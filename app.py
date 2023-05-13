from flask import Flask
from flask_restful import Api
#from flask_sqlalchemy import SQLAlchemy

from views.todos_views import todo_bp
from views.user_views import user_bp

app = Flask(__name__)
api = Api(app, prefix='/api/v1')


app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(todo_bp, url_prefix='/todos')
