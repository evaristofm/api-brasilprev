import uuid
from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel


class ClienteRequest(BaseModel):
    nome: str
    cpf: str
    email: str
    genero: str
    dataDeNascimento: datetime
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
