from sqlalchemy import select
from database import nova_sessao
from models.entidades import Produto

def listar_todos_produtos():
    with nova_sessao() as session:
        statement = select(Produto)
        return list(session.scalars(statement).all())

def buscar_produtos_por_nome(nome):
    with nova_sessao() as session:
        termo = f"%{nome.strip()}%"
        statement = select(Produto).where(Produto.nome.ilike(termo))
        return list(session.scalars(statement).all())

def buscar_produtos_por_categoria(categoria):
    with nova_sessao() as session:
        termo = f"%{categoria.strip()}%"
        statement = select(Produto).where(Produto.categoria.ilike(termo))
        return list(session.scalars(statement).all())

def buscar_produto_por_id(produto_id):
    with nova_sessao() as session:
        return session.get(Produto, produto_id)