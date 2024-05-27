import uuid
from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel


class ClienteRequest(BaseModel):
    cpf: str
    nome: str
    email: str
    dataDeNascimento: datetime
    genero: str
    rendaMensal: float


class ClienteResponse(ClienteRequest):
    ...


class ClienteResponseId(BaseModel):
    id: uuid.UUID


class ProdutoRequest(BaseModel):
    nome: str 
    susep: str 
    expiracaoDeVenda: datetime 
    valorMinimoAporteInicial: float 
    valorMinimoAporteExtra: float 
    idadeDeEntrada: int
    idadeDeSaida: int
    carenciaInicialDeResgate: int
    carenciaEntreResgates: int


class ProdutoResponseId(BaseModel):
    id: uuid.UUID


class PlanoRequest(BaseModel):
    idCliente: uuid.UUID
    idProduto: uuid.UUID
    aporte: float 
    dataDaContratacao: datetime 
    idadeDeAposentadoria: int 


class PlanoResponseId(BaseModel):
    id: uuid.UUID


class AporteExtraRequest(BaseModel):
    idCliente: uuid.UUID
    idPlano: uuid.UUID
    valorAporte: Decimal


class AporteExtraIdResponse(BaseModel):
    id: uuid.UUID


class ResgateRequest(BaseModel):
    idPlano: uuid.UUID
    valorResgate: Decimal


class ResgateIdResponse(BaseModel):
    id: uuid.UUID



datetime.strptime("2024-06-01 01:48:30.650779", "%Y-%m-%d %H:%M:%S.%f") - datetime.strptime("1996-03-05 01:48:30.650779", "%Y-%m-%d %H:%M:%S.%f")