from sqlalchemy import select
from database import nova_sessao
from models.entidades import *
from flask import flash


def listar_carrinho(usuario_id):
    with nova_sessao() as session:
        stmt = (select(Produto).join(Produto.carrinho).where(Carrinho.usuario_id == usuario_id))
        return list(session.scalars(stmt).all())

def adicionar_carrinho(usuario_id,produto_id):
    with nova_sessao() as session:
        produto = session.get(Produto, produto_id)
        if produto is None:
            flash('O produto não existe')
        carrinho = session.scalar(
            select(Carrinho).where(Carrinho.usuario_id == usuario_id)
        )
        if carrinho is None:
            carrinho = Carrinho(usuario_id = usuario_id)
            session.add(carrinho)
        if produto not in carrinho.produtos:
            carrinho.produtos.append(produto)
        session.commit()