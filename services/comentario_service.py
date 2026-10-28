from sqlalchemy import select
from sqlalchemy.orm import joinedload
from database import nova_sessao
from models.entidades import Comentario

def listar_comentarios():
    with nova_sessao() as session:
        statement = select(Comentario).options(joinedload(Comentario.produto)).order_by(Comentario.id)
        return list(session.scalars(statement).all())
