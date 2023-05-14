# Todo App API

This is a Todo App API that provides endpoints for managing Todo items. It is built using Python 3 and the Flask web framework. The API is designed to be RESTful and follows the principles of HTTP.

## Design Pattern

This project follows the Model-View-Controller (MVC) design pattern.
Model: The model represents the data and the business logic of the application. In this project, the model is represented by the database schema and the ORM (Object-Relational Mapping) framework SQLAlchemy.

View: The view is responsible for presenting the data to the user and receiving user input. In this project, the view is represented by the Flask routes, which receive HTTP requests and return HTTP responses in JSON format.

Controller: The controller is responsible for handling the user input and manipulating the data in the model.

## API Endpoints

- `POST /todos`: Create a new todo
- `GET /todos`: Retrieve all todos
- `GET /todos/{id}`: Retrieve a single todo
- `PUT /todos/{id}`: Update a todo
- `DELETE /todos/{id}`: Delete a todo
- `POST /users/signup`: Sign up a new user
- `POST /users/login`: Log in an existing user
- `GET /users/me`: Retrieve the currently logged in user
- `GET /users`: Retrieve all users

## Security

This API is not yet fully secure. Future updates will include the use of access tokens for authentication and authorization.

