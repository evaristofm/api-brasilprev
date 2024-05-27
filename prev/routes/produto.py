import uuid
from typing import List
from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from sqlmodel import Session, select

from prev.db import ActiveSession
from prev.models.user import Produto
from prev.serializers import ProdutoRequest, ProdutoResponseId



router = APIRouter()


@router.get("/", response_model=List[ProdutoRequest])
async def list_users(*, session: Session = ActiveSession):
    """Lista produtos."""
    clientes = session.exec(select(Produto)).all()
    return clientes


@router.post("/", response_model=ProdutoResponseId, status_code=status.HTTP_201_CREATED)
async def create_user(*, session: Session = ActiveSession, cliente: ProdutoRequest):
    """Criar novos produtos"""
    db_produto = Produto(**cliente.model_dump(), id=uuid.uuid4())
    session.add(db_produto)
    session.commit()
    session.refresh(db_produto)
    return db_produto
