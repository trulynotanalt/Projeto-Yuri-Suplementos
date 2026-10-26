from sqlalchemy import select
from database import nova_sessao
from models.entidades import *
from flask import flash
from datetime import date


def listar_compra(usuario_id):
    with nova_sessao() as session:
        stmt = (select(Produto).join(Produto.compras).where(Compra.usuario_id == usuario_id))
        return list(session.scalars(stmt).all())

def adicionar_compra(usuario_id,produto_id):
    with nova_sessao() as session:
        produto = session.get(Produto, produto_id)
        if produto is None:
            flash('O produto não existe')
        compra = session.scalar(
            select(Compra).where(Compra.usuario_id == usuario_id)
        )
        if compra is None:
            compra = Compra(
                usuario_id=usuario_id,
                descricao=Produto.informacao,
                data_criacao=date.today())
            session.add(compra)
        if produto not in compra.produtos_compra:
            compra.produtos_compra.append(produto)
        session.commit()