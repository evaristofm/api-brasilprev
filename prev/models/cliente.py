import uuid as uuid_pkg
from decimal import Decimal
from datetime import datetime
from sqlmodel import Field, SQLModel


class Cliente(SQLModel, table=True):
    id: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.UUID,
        primary_key=True,
        index=True,
        nullable=False)
    nome: str = Field(nullable=False)
    cpf: str = Field(unique=True, nullable=False)
    email: str = Field(unique=True, nullable=False)
    dataDeNascimento: datetime = Field(nullable=False)
    genero: str = Field(nullable=False)
    rendaMensal: Decimal = Field(default=0)