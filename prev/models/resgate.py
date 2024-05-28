import uuid as uuid_pkg
from decimal import Decimal
from datetime import datetime
from sqlmodel import Field, SQLModel



class Resgate(SQLModel, table=True):
    id: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.UUID, 
        primary_key=True,
        index=True, 
        nullable=False)
    idPlano: uuid_pkg.UUID = Field(foreign_key="plano.id")
    valorResgate: Decimal = Field(default=0)