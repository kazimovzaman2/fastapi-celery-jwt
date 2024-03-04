from pydantic import BaseModel


class UserSchema(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str

    class Config:
        json_schema_extra = {
            "example": {
                "first_name": "Zaman",
                "last_name": "Kazimov",
                "email": "kazimovzaman2@gmail.com",
                "password": "password",
            }
        }


class LoginSchema(BaseModel):
    email: str
    password: str

    class Config:
        json_schema_extra = {
            "example": {
                "email": "kazimovzaman2@gmail.com",
                "password": "password",
            }
        }
