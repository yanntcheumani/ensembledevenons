from pydantic import BaseModel

class ItemBase(BaseModel):
    name: str

class ItemCreate(ItemBase):
    """Hérité de ItemBase, utilisé pour la création."""
    pass

class ItemRead(ItemBase):
    id: int

    class Config:
        orm_mode = True
        """Permet la compatibilité avec SQLAlchemy ORM."""
