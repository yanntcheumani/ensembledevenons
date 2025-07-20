from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str
    """On ajoute le mot de passe pour la création."""

class UserRead(UserBase):
    id: int

    class Config:
        orm_mode = True
