from sqlalchemy import select, update,insert,delete
from database import nova_sessao
from models.entidades import *
from flask import flash


def listar_carrinho(usuario_id):
    with nova_sessao() as session:
        stmt = (
            select(Produto, carrinho_produto.c.quantidade)
            .join(
                carrinho_produto,
                Produto.id == carrinho_produto.c.produto_id
            )
            .join(
                Carrinho,
                Carrinho.id == carrinho_produto.c.carrinho_id
            )
            .where(Carrinho.usuario_id == usuario_id)
        )

        return session.execute(stmt).all()

def adicionar_carrinho(usuario_id,produto_id):
    with nova_sessao() as session:
        produto = session.get(Produto, produto_id)
        if produto is None:
            return flash('O produto não existe')
        carrinho = session.scalar(
            select(Carrinho).where(Carrinho.usuario_id == usuario_id)
        )
        if carrinho is None:
            carrinho = Carrinho(usuario_id = usuario_id)
            session.add(carrinho)
            session.flush()

        stmt = (update(carrinho_produto).where(carrinho_produto.c.carrinho_id == carrinho.id,
            carrinho_produto.c.produto_id == produto_id).values(
                quantidade= carrinho_produto.c.quantidade + 1
            ))
        
        resultado =session.execute(stmt)
        if resultado.rowcount == 0:
            session.execute(
                insert(carrinho_produto).values(
                    carrinho_id=carrinho.id,
                    produto_id=produto_id
                )
            )
        
        session.commit()

def remover_carrinho(usuario_id,produto_id):
    with nova_sessao() as session:
        produto = session.get(Produto, produto_id)
        carrinho = session.scalar(
            select(Carrinho).where(Carrinho.usuario_id == usuario_id)
        )
        if produto not in carrinho.produtos:
            return flash('produto n esta no carrinho')
        carrinho.produtos.remove(produto)
        session.commit()

def retirar_carrinho(usuario_id,produto_id):
    with nova_sessao() as session:
        carrinho = session.scalar(
            select(Carrinho).where(Carrinho.usuario_id == usuario_id)
        )

        
        stmt = select(carrinho_produto.c.quantidade).where(
            carrinho_produto.c.carrinho_id == carrinho.id,
            carrinho_produto.c.produto_id == produto_id
        )

        quantidade = session.scalar(stmt)        
  
        if quantidade <= 1:
            session.execute(
                delete(carrinho_produto).where(
                    carrinho_produto.c.carrinho_id == carrinho.id,
                    carrinho_produto.c.produto_id == produto_id
                )
            )
        else:
            session.execute(
                update(carrinho_produto)
                .where(
                    carrinho_produto.c.carrinho_id == carrinho.id,
                    carrinho_produto.c.produto_id == produto_id
                )
                .values(
                    quantidade=carrinho_produto.c.quantidade - 1
                )
            )


        session.commit()
