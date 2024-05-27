from datetime import datetime
from typing import List
from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from sqlmodel import Session

from prev.routes import crud
from prev.db import ActiveSession
from prev.serializers import PlanoRequest, PlanoResponseId, AporteExtraRequest, AporteExtraIdResponse



router = APIRouter()


# @router.get("/", response_model=List[PlanoRequest])
# async def list_users(*, session: Session = ActiveSession):
#     """Lista planos."""
#     clientes = crud.get_plano_all(db=session)
#     return clientes


@router.post("/", response_model=PlanoResponseId, status_code=201)
async def create_plano(*, session: Session = ActiveSession, plano_request: PlanoRequest):
    """Criar novos planos"""
    db_produto = crud.get_produto(db=session, producto_id=plano_request.idProduto)

    if not db_produto:
        raise HTTPException(status_code=404, detail="Producto não encontrado!")
    if db_produto.expiracaoDeVenda < datetime.now():
        raise HTTPException(status_code=400, detail="Data de venda do produto expirado")
    if plano_request.aporte < db_produto.valorMinimoAporteInicial:
        raise HTTPException(status_code=400, detail="A contribuição inicial é inferior ao mínimo exigido")
    

    #TODO: Adicionar regras de idade, entrada e saida
    
    db_plano = crud.create_plano(db=session, plano=plano_request)
    return db_plano


