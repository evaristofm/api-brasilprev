from datetime import datetime
from typing import List
from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from sqlmodel import Session, select

from prev.routes import crud
from prev.models.plano import Plano
from prev.db import ActiveSession
from prev.serializers import PlanoRequest, PlanoResponseId, AporteExtraRequest, AporteExtraIdResponse



router = APIRouter()


@router.get("/", response_model=List[PlanoRequest])
async def get_plano_all(*, session: Session = ActiveSession):
    """Lista planos."""
    planos = session.exec(select(Plano)).all()
    return planos


@router.post("/", response_model=PlanoResponseId, status_code=201)
async def create_plano(*, session: Session = ActiveSession, plano_request: PlanoRequest):
    """Criar novos planos"""
    db_produto = crud.get_produto(db=session, producto_id=plano_request.idProduto)
    db_cliente = crud.get_cliente(db=session, cliente_id=plano_request.idCliente)

    if not db_produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado!")
    
    if db_produto.expiracaoDeVenda < datetime.now():
        raise HTTPException(status_code=400, detail="Data de venda do produto expirado")

    if plano_request.aporte < db_produto.valorMinimoAporteInicial:
        raise HTTPException(status_code=400, detail="A contribuição inicial é inferior ao mínimo exigido.")
    
    idade =  datetime.now().year - db_cliente.dataDeNascimento.year

    if idade < db_produto.idadeDeEntrada or idade > db_produto.idadeDeSaida:
        raise HTTPException(status_code=400, detail="Idade do cliente não permitida para a contratação do plano.")
    
    db_plano = crud.create_plano(db=session, plano=plano_request)
    
    return db_plano


