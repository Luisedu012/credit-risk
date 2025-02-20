import pytest
from unittest.mock import MagicMock
from database.database import get_connection
import psycopg2

def test_get_connection_success(mocker):
    """Testa se a conexão é estabelecida corretamente e a consulta SELECT é executada."""
    mock_conn = MagicMock(spec=psycopg2.extensions.connection)
    mock_cursor = MagicMock(spec=psycopg2.extensions.cursor)
    mock_connect = mocker.patch("psycopg2.connect", return_value=mock_conn)
    mock_conn.cursor.return_value = mock_cursor

    conn = get_connection()

    assert conn is not None, "A conexão deveria ser estabelecida com sucesso"
    assert mock_connect.called, "psycopg2.connect deveria ter sido chamado"
    assert isinstance(conn, psycopg2.extensions.connection), "O retorno deve ser um objeto de conexão"

    mock_cursor.execute.return_value = None
    mock_cursor.fetchall.return_value = [{"id": 1, "nome": "Cliente1"}, {"id": 2, "nome": "Cliente2"}]

    mock_cursor.execute("SELECT * FROM Clientes")
    result = mock_cursor.fetchall()

    mock_cursor.execute.assert_called_with("SELECT * FROM Clientes")
    assert result == [{"id": 1, "nome": "Cliente1"}, {"id": 2, "nome": "Cliente2"}], "O retorno da consulta está incorreto"

def test_get_connection_operational_error(mocker):
    """Testa se um erro operacional (ex: banco offline) é tratado corretamente."""
    mock_connect = mocker.patch("psycopg2.connect", side_effect=psycopg2.OperationalError("Banco offline"))

    conn = get_connection()

    assert conn is None, "Deveria retornar None quando ocorrer um erro operacional"
    assert mock_connect.called, "A função psycopg2.connect deveria ter sido chamada"

def test_get_connection_generic_error(mocker):
    """Testa se um erro inesperado é tratado corretamente."""
    mock_connect = mocker.patch("psycopg2.connect", side_effect=Exception("Erro desconhecido"))

    conn = get_connection()

    assert conn is None, "Deveria retornar None quando ocorrer um erro genérico"
    assert mock_connect.called, "A função psycopg2.connect deveria ter sido chamada"
