import os
import pytest
from fastapi.testclient import TestClient
from fastapi import Depends
from sqlmodel import create_engine, Session, SQLModel

from prev.models.cliente import Cliente
from prev.config import settings
from prev.db import get_session
from prev.app import app

os.environ["DUNDIE_DB__uri"] = "postgresql://postgres:postgres@db:5432/dundie_test"


@pytest.fixture(scope="function")
def api_client():
    """Unauthenticated test client"""
    return TestClient(app)
