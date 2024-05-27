import uuid
from typing import List
from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from sqlmodel import Session, select

from prev.db import ActiveSession
from prev.models.user import Plano
from prev.serializers import PlanoRequest, PlanoResponseId



router = APIRouter()


@router.get("/", response_model=List[PlanoRequest])
async def list_users(*, session: Session = ActiveSession):
    """Lista planos."""
    clientes = session.exec(select(Plano)).all()
    return clientes


@router.post("/", response_model=PlanoResponseId, status_code=status.HTTP_201_CREATED)
async def create_user(*, session: Session = ActiveSession, cliente: PlanoRequest):
    """Criar novos planos"""
    db_plano = Plano(**cliente.model_dump(), id=uuid.uuid4())
    session.add(db_plano)
    session.commit()
    session.refresh(db_plano)
    return db_plano
