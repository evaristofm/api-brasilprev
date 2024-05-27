import uuid
from typing import List
from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from sqlmodel import Session, select

from prev.db import ActiveSession
from prev.models.user import Resgate
from prev.serializers import ResgateRequest, ResgateIdResponse



router = APIRouter()


@router.get("/", response_model=List[ResgateRequest])
async def list_users(*, session: Session = ActiveSession):
    """Lista regates."""
    aportes = session.exec(select(Resgate)).all()
    return aportes


@router.post("/", response_model=ResgateIdResponse, status_code=status.HTTP_201_CREATED)
async def create_user(*, session: Session = ActiveSession, cliente: ResgateRequest):
    """Criar novos resgates"""
    db_resgate = Resgate(**cliente.model_dump(), id=uuid.uuid4())
    session.add(db_resgate)
    session.commit()
    session.refresh(db_resgate)
    return db_resgate
