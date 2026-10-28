from sqlalchemy import select
from database import nova_sessao
from models.entidades import *
from flask import flash
from datetime import date


def listar_compra(usuario_id):
    with nova_sessao() as session:
        stmt = (select(Compra).where(Compra.usuario_id == usuario_id))
        compras = list(session.scalars(stmt).all())

        for compra in compras:
            list(compra.produtos_compra)

        return compras

def adicionar_compra(usuario_id,produto_id):
    with nova_sessao() as session:
        produto = session.get(Produto, produto_id)
        if produto is None:
            flash('O produto não existe')
        compra = session.scalar(
            select(Compra).where(Compra.usuario_id == usuario_id)
        )
        
        if produto.comentarios:
            descricao = produto.comentarios[0].texto
        else:
            descricao = 'produto bom'
        
        if compra is None:
            compra = Compra(
                usuario_id=usuario_id,
                descricao=descricao,
                data_criacao=date.today())
            session.add(compra)
        if produto not in compra.produtos_compra:
            compra.produtos_compra.append(produto)
        session.commit()