import uuid
from typing import List
from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from sqlmodel import Session, select

from prev.db import ActiveSession
from prev.models.user import Cliente
from prev.serializers import ClienteRequest, ClienteResponseId, ClienteResponse


router = APIRouter()


@router.get("/", response_model=List[ClienteResponse])
async def get_all_clientes(*, session: Session = ActiveSession):
    """List all users."""
    clientes = session.exec(select(Cliente)).all()
    return clientes


@router.post("/", response_model=ClienteResponseId, status_code=status.HTTP_201_CREATED)
async def create_cliente(*, session: Session = ActiveSession, cliente: ClienteRequest):
    """Criar novos clientes"""
    db_cliente = Cliente(**cliente.model_dump(), id=uuid.uuid4())
    session.add(db_cliente)
    session.commit()
    session.refresh(db_cliente)
    return db_cliente

