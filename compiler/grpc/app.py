from compiler.grpc import server
from dotenv import load_dotenv
from pathlib import Path


def run():
    env_path = Path('.') / '/opt/compiler/.env'
    load_dotenv(dotenv_path=env_path)

    server.serve()