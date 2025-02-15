import os
from dotenv import load_dotenv

load_dotenv()

DB_URL = os.getenv("URL_DB")
USER_DB = os.getenv("user_DB")
PASSWORD_DB = os.getenv("password_DB")
HOST_DB = os.getenv("host_DB")
PORT_DB = os.getenv("port")
DBNAME = os.getenv("DBNAME")