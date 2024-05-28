import uuid as uuid_pkg
from decimal import Decimal
from datetime import datetime
from sqlmodel import Field, SQLModel


class Produto(SQLModel, table=True):
    id: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.UUID,
        primary_key=True,
        index=True,
        nullable=False)
    nome: str = Field(nullable=False)
    susep: str = Field(nullable=False)
    expiracaoDeVenda: datetime = Field(nullable=False)
    valorMinimoAporteInicial: Decimal = Field(default=0)
    valorMinimoAporteExtra: Decimal = Field(default=0)
    idadeDeEntrada: int = Field(nullable=False)
    idadeDeSaida: int = Field(nullable=False)
    carenciaInicialDeResgate: int = Field(nullable=False)
    carenciaEntreResgates: int = Field(nullable=False)