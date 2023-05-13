from typing import List

from pydantic import BaseModel
from pydantic import EmailStr

from schema.todo_schema import TodoSchema

class Userbase(BaseModel):
    email:EmailStr

class UserSchema(Userbase):
    first_name:str
    last_name:str

    class Config:
        orm_mode=True

class CreateSchema(UserSchema):
    password:str
    #set to False because it is a Pydantic model used to receive input data from the client ( via a POST request), 
    # and the input data does not need to be serialized to the database. 
    class Config:
        orm_mode=False


class UserFullSchema(UserSchema):
    todos: List[TodoSchema]

    
