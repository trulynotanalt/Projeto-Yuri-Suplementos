from sqlalchemy import select,update,insert
from database import nova_sessao
from models.entidades import *
from flask import flash
from datetime import date


def listar_compra(usuario_id):
    with nova_sessao() as session:
        stmt = (
            select(Compra, Produto, compra_produto.c.quantidade)
            .join(
                compra_produto,
                Compra.id == compra_produto.c.compra_id
            )
            .join(
                Produto,
                Produto.id == compra_produto.c.produto_id
            )
            .where(Compra.usuario_id == usuario_id)
        )

        return session.execute(stmt).all()

def adicionar_compra(usuario_id,produto_id, quantidade=1):
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
                descricao='Compra',
                data_criacao=date.today())
            session.add(compra)
            session.flush()

        stmt = select(compra_produto.c.quantidade).where(
            compra_produto.c.compra_id == compra.id,
            compra_produto.c.produto_id == produto_id
        )

        quantidade_atual = session.scalar(stmt)
        quantidade = int(quantidade or 1)

        if quantidade_atual is None:
            session.execute(
                insert(compra_produto).values(
                    compra_id=compra.id,
                    produto_id=produto_id,
                    quantidade=quantidade
                )
            )
        else:
            session.execute(
                update(compra_produto)
                .where(
                    compra_produto.c.compra_id == compra.id,
                    compra_produto.c.produto_id == produto_id
                )
                .values(
                    quantidade=quantidade_atual + quantidade
                )
            )

        session.commit()