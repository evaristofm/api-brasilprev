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
    rendaMensal: Decimal


class ClienteResponse(ClienteRequest):
    ...


class ClienteResponseId(BaseModel):
    id: uuid.UUID


class ProdutoRequest(BaseModel):
    nome: str 
    susep: str 
    expiracaoDeVenda: datetime 
    valorMinimoAporteInicial: Decimal 
    valorMinimoAporteExtra: Decimal 
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
    valorAporte: float


class AporteExtraIdResponse(BaseModel):
    id: uuid.UUID


class ResgateRequest(BaseModel):
    idPlano: uuid.UUID
    valorResgate: float


class ResgateIdResponse(BaseModel):
    id: uuid.UUID
    