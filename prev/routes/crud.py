import uuid
from sqlmodel import Session, select

from prev.models.user import Cliente, Produto, Plano, AporteExtra, Resgate
from prev import serializers


def create_cliente(db: Session, cliente: serializers.ClienteRequest):
    db_cliente = Cliente(**cliente.model_dump(), id=uuid.uuid4())
    
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente


def create_produto(db: Session, produto: serializers.ProdutoRequest):
    db_produto = Produto(**produto.model_dump(), id=uuid.uuid4())

    db.add(db_produto)
    db.commit()
    db.refresh(db_produto)
    return db_produto

def create_plano(db: Session, plano: serializers.PlanoRequest):
    db_plano = Plano(**plano.model_dump(), id=uuid.uuid4())

    db.add(db_plano)
    db.commit()
    db.refresh(db_plano)
    return db_plano

def create_aporte_extra(db: Session, aporte: serializers.AporteExtraRequest):
    db_aporte = AporteExtra(**aporte.model_dump(), id=uuid.uuid4())

    db.add(db_aporte)
    db.commit()
    db.refresh(db_aporte)
    return db_aporte

def create_resgate(db: Session, resgate: serializers.ResgateRequest):
    db_resgate = Resgate(**resgate.model_dump(), id=uuid.uuid4())

    db.add(db_resgate)
    db.commit()
    db.refresh(db_resgate)

    return db_resgate


def get_cliente_all(db: Session, cliente_id: str):
    return db.query(Cliente).all()

def get_cliente(db: Session, cliente_id: str):
    return db.query(Cliente).filter(Cliente.id == cliente_id).first()

def get_produto_all(db: Session):
    return db.query(Produto).all()

def get_produto(db: Session, producto_id: str):
    return db.query(Produto).filter(Produto.id == producto_id).first()

def get_plano_all(db: Session):
    return db.query(Plano).all()

def get_plano(db: Session, plano_id: str):
    return db.query(Plano).filter(Plano.id == plano_id).first()