from typing import List
from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from sqlmodel import Session, select

from prev.routes import crud
from prev.db import ActiveSession
from prev.models.user import AporteExtra
from prev.serializers import AporteExtraRequest, AporteExtraIdResponse



router = APIRouter()


@router.get("/", response_model=List[AporteExtraRequest])
async def get_aportes_all(*, session: Session = ActiveSession):
    """Lista aportes."""
    aportes = session.exec(select(AporteExtra)).all()
    return aportes


@router.post("/", response_model=AporteExtraIdResponse, status_code=201)
async def create_apote_extra(*, session: Session = ActiveSession, aporte_extra: AporteExtraRequest):
    """Criar novos aportes"""

    db_plano = crud.get_plano(db=session, plano_id=aporte_extra.idPlano)

    if not db_plano:
        raise HTTPException(status_code=404, detail="Plano não encontrado!")
    
    db_produto = crud.get_produto(db=session, producto_id=db_plano.idProduto)
          
    if aporte_extra.valorAporte < db_produto.valorMinimoAporteExtra:
        raise HTTPException(status_code=400, detail="A contribuição adicional é inferior ao mínimo exigido")

    db_plano.aporte += aporte_extra.valorAporte

    db_aporte_extra = crud.create_aporte_extra(db=session, aporte=aporte_extra)

    session.commit()
    session.refresh(db_plano)

    return db_aporte_extra
