# Example 2-2. Validating user passwords in FastAPI using a Pydantic schema

from pydantic import BaseModel, Field, EmailStr
from fastapi import FastAPI

class UserCreate(BaseModel):
    username: str
    password: str

    @validator('password')
    def validate_password(cls, value):
        if len(value) < 8:
            raise ValueError('Password must be at least 8 characters long')
        if not any(char.isdigit() for char in value):
            raise ValueError('Password must contain at least one digit')
        if not any(char.isupper() for char in value):
            raise ValueError('Password must contain at least one uppercase letter')
        return value 

app = FastAPI()

@app.post("/users/")
async def create_user_controller(user: UserCreate):
    return {
        "name": user.name,
        "message": "Account created successfully"
    }