import uuid as uuid_pkg
from decimal import Decimal
from datetime import datetime
from sqlmodel import Field, SQLModel


class Plano(SQLModel, table=True):
    id: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.UUID,
        primary_key=True,
        index=True,
        nullable=False)
    
    idCliente: uuid_pkg.UUID = Field(foreign_key="cliente.id")
    idProduto: uuid_pkg.UUID = Field(foreign_key="produto.id")
    aporte: Decimal = Field(default=0)
    dataDaContratacao: datetime = Field(nullable=False)
    idadeDeAposentadoria: int = Field(nullable=False)