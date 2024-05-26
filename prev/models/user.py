import uuid as uuid_pkg
from decimal import Decimal
from datetime import datetime
from sqlmodel import Field, SQLModel, Relationship


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


class Plano(SQLModel, table=True):
    id: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.UUID,
        primary_key=True,
        index=True,
        nullable=False)
    
    idCliente: uuid_pkg.UUID = Field(foreign_key="cliente.id")
    idProduto: uuid_pkg.UUID = Field(foreign_key="produto.id")

    aporte: str = Field(nullable=False)
    dataDaContratacao: datetime = Field(nullable=False)
    idadeDeAposentadoria: int = Field(nullable=False)


class Resgate(SQLModel, table=True):
    id: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.UUID, 
        primary_key=True,
        index=True, 
        nullable=False)
    idPlano: uuid_pkg.UUID = Field(foreign_key="plano.id")
    valorResgate: Decimal = Field(default=0)


class AporteExtra(SQLModel, table=True):
    id: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.UUID,
        primary_key=True,
        index=True,
        nullable=False)
    
    idCliente: uuid_pkg.UUID= Field(foreign_key="cliente.id")
    idPlano: uuid_pkg.UUID = Field(foreign_key="plano.id")
    valorAporte: Decimal = Field(default=0)
