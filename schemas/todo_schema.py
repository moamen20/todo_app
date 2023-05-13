from pydantic import BaseModel


class TodoBaseSchema(BaseModel):
    text: str
    completed: bool


class TodoSchema(TodoBaseSchema):
    owner_id: int
    #setting orm_mode to True, 
    #Pydantic will generate the model to handle attributes that are not part of the original Pydantic schema but are part of the ORM model.
    class Config:
        orm_mode = True


class TodoResponseSchema(TodoSchema):
    id: int


class TodoUpdateSchema(TodoBaseSchema):
    id: int

