import uuid
import typer
from datetime import datetime
from rich.console import Console
from rich.table import Table
from sqlmodel import Session, select

from .config import settings
from .db import engine
from .models import Cliente

main = typer.Typer(name="prev CLI", add_completion=False)

@main.command()
def shell():
    """Opens interactive shell"""
    _vars = {
        "settings": settings,
        "engine": engine,
        "select": select,
        "session": Session(engine),
        "Cliente": Cliente,
    }
    typer.echo(f"Auto imports: {list(_vars.keys())}")
    try:
        from IPython import start_ipython

        start_ipython(
            argv=["--ipython-dir=/tmp", "--no-banner"], user_ns=_vars
        )
    except ImportError:
        import code

        code.InteractiveConsole(_vars).interact()

@main.command()
def cliente_list():
    """Lists all users"""
    table = Table(title="dundie users")
    fields = ["nome", "cpf", "email", "dataDeNascimento", "genero", "rendaMensal"]
    for header in fields:
        table.add_column(header, style="magenta")

    with Session(engine) as session:
        clientes = session.exec(select(Cliente))
        for cliente in clientes:
            table.add_row(*[getattr(cliente, field) for field in fields])

    Console().print(table)

@main.command()
def create_cliente(
    nome: str,
    cpf: str,
    email: str,
    genero: str,
    rendamensal: str,
):
    """Create cliente"""
    with Session(engine) as session:
        cliente = Cliente(
            id=uuid.uuid4(),
            nome=nome,
            cpf=cpf,
            email=email,
            dataDeNascimento=datetime.now(),
            genero=genero.casefold(),
            rendaMensal=float(rendamensal),
        )
        session.add(cliente)
        session.commit()
        session.refresh(cliente)
        typer.echo(f"created {cliente.nome} cliente")
        return cliente