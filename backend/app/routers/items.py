from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from .. import models
from ..schemas import ItemCreate, ItemRead
from ..database import get_db

router = APIRouter(prefix="/items", tags=["items"])

@router.get("/", response_model=list[ItemRead])
async def read_items(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Item))
    return result.scalars().all()

@router.post("/", response_model=ItemRead, status_code=status.HTTP_201_CREATED)
async def create_item(item: ItemCreate, db: AsyncSession = Depends(get_db)):
    db_item = models.Item(**item.dict())
    db.add(db_item)
    await db.commit()
    await db.refresh(db_item)
    return db_item
