import uuid as uuid_pkg
from decimal import Decimal
from sqlmodel import Field, SQLModel



class AporteExtra(SQLModel, table=True):
    id: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.UUID,
        primary_key=True,
        index=True,
        nullable=False)
    
    idCliente: uuid_pkg.UUID= Field(foreign_key="cliente.id")
    idPlano: uuid_pkg.UUID = Field(foreign_key="plano.id")
    valorAporte: Decimal = Field(default=0)