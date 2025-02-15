# tests/test_db_connection.py
import pytest
from sqlalchemy.exc import OperationalError
from database.database import engine, DATABASE_URL

def test_database_connection():
    """Teste simples para verificar a conexão com o banco de dados."""
    assert DATABASE_URL, "A variável de ambiente DATABASE_URL está vazia."

    try:
        with engine.connect() as connection:
            assert connection.closed is False
    except OperationalError:
        pytest.fail('Database connection failed.')

