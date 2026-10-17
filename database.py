from sqlalchemy import create_engine
from sqlalchemy.orm import Session, DeclarativeBase

engine = create_engine("sqlite:///database.db")

class Base(DeclarativeBase):
    pass

def criar_banco():
    Base.metadata.create_all(bind=engine)

def nova_sessao():
    return Session(bind=engine)
