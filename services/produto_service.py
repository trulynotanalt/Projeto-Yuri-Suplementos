from sqlalchemy import select, func
from database import nova_sessao
from models.entidades import Produto, Compra,compra_produto

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

def listar_sugestoes():
    with nova_sessao() as session:
        statement = select(Produto).order_by(func.random()).limit(8)
        return list(session.scalars(statement).all())

def listar_produtos_comprados(usuario_id):
    with nova_sessao() as session:
        statement = (
            select(
                Compra,
                Produto,
                compra_produto.c.quantidade
            )
            .join(compra_produto, Compra.id == compra_produto.c.compra_id)
            .join(Produto, Produto.id == compra_produto.c.produto_id)
            .where(Compra.usuario_id == usuario_id)
        )
        return session.execute(statement).all()  

def buscar_produto_por_id(produto_id):
    with nova_sessao() as session:
        return session.get(Produto, produto_id)