from fastapi import FastAPI
from .database import engine, Base
from .routers import items  # on pourra ajouter users.py

app = FastAPI(title="API END", version="1.0.0")

@app.on_event("startup")
async def on_startup():
    # création automatique des tables pour tous les modèles importés
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.include_router(items.router)
# app.include_router(users.router)  # quand votre router users existera
