from fastapi import FastAPI

from .routes import main_router


app = FastAPI(
    title='BrasilPrev',
    version='0.1.0',
    description='Api plano de previdência privada'
)

app.include_router(main_router)
