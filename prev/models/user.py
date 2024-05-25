import uuid 
from decimal import Decimal
from datetime import datetime
from typing import Optional
from sqlmodel import Field, SQLModel


class Cliente(SQLModel, table=True):
    
    id: uuid.UUID = Field(
        default_factory=uuid.uuid4, 
        primary_key=True,
        index=True, 
        nullable=False)
    nome: str = Field(nullable=False)
    cpf: str = Field(unique=True, nullable=False)
    email: str = Field(unique=True, nullable=False)
    dataDeNascimento: datetime = Field(nullable=False)
    genero: str = Field(nullable=False)
    rendaMensal: Decimal = Field(default=0)
    