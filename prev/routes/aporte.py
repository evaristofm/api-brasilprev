import uuid
from typing import List
from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from sqlmodel import Session, select

from prev.db import ActiveSession
from prev.models.user import AporteExtra
from prev.serializers import AporteExtraRequest, AporteExtraIdResponse



router = APIRouter()


@router.get("/", response_model=List[AporteExtraRequest])
async def list_users(*, session: Session = ActiveSession):
    """Lista aportes."""
    aportes = session.exec(select(AporteExtra)).all()
    return aportes


@router.post("/", response_model=AporteExtraIdResponse, status_code=status.HTTP_201_CREATED)
async def create_user(*, session: Session = ActiveSession, cliente: AporteExtraRequest):
    """Criar novos aportes"""
    db_aporte = AporteExtra(**cliente.model_dump(), id=uuid.uuid4())
    session.add(db_aporte)
    session.commit()
    session.refresh(db_aporte)
    return db_aporte
