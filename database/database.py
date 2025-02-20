
import os
import psycopg2
import psycopg2.extensions
from dotenv import load_dotenv
from typing import Optional
from urllib.parse import urlparse

load_dotenv()

def get_connection() -> Optional[psycopg2.extensions.connection]:
    """Estabelece conexão segura com o banco PostgreSQL via URL.

    Returns:
        Optional[psycopg2.extensions.connection]: Objeto de conexão se bem-sucedido, None caso contrário.
    """
    try:
        db_url = os.getenv("URL_DB")
        if not db_url:
            raise ValueError("A variável de ambiente URL_DB não está definida.")

        parsed_url = urlparse(db_url)

        conn = psycopg2.connect(
            dbname=parsed_url.path.lstrip('/'),
            user=parsed_url.username,
            password=parsed_url.password,
            host=parsed_url.hostname,
            port=parsed_url.port,
            connect_timeout=10
        )
        return conn
    except psycopg2.OperationalError as e:
        print(f"[Erro de Conexão] {e}")
    except psycopg2.Error as e:
        print(f"[Erro no Banco] {e}")
    except Exception as e:
        print(f"[Erro Desconhecido] {e}")

    return None
