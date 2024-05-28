from fastapi import APIRouter

from .cliente import router as cliente_router
from .produto import router as produto_router
from .plano import router as plano_router
from .aporte import router as aporte_router
from .resgate import router as resgate_router

main_router = APIRouter()

main_router.include_router(cliente_router, prefix="/cliente", tags=["clientes"])
main_router.include_router(produto_router, prefix="/produto", tags=["produtos"])
main_router.include_router(plano_router, prefix="/plano", tags=["planos"])
main_router.include_router(aporte_router, prefix="/aporte", tags=["aportes"])
main_router.include_router(resgate_router, prefix="/resgate", tags=["resgates"])



