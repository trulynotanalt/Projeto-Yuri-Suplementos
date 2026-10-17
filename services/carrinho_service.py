from sqlalchemy import select
from database import nova_sessao
from models.entidades import *

def listar_carrinho(usuario_id):
    with nova_sessao() as session:
        statement = select(Carrinho.produtos).where(Carrinho.usuario_id == usuario_id)
        return list(session.scalars(statement).all())