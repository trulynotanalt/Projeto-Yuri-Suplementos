from typing import List, Optional
from sqlalchemy import String, Float, ForeignKey, Table, Column, Date, CheckConstraint, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base

class Usuario(Base):
    __tablename__ = 'usuario'

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(60), nullable = False)
    email: Mapped[str] = mapped_column(String(90), unique=True, nullable = False)
    senha_hash: Mapped[str] = mapped_column(String(220), nullable = False)

    carrinho: Mapped[List['Carrinho']] = relationship(back_populates='usuario')
    compras: Mapped[List['Compra']] = relationship(back_populates='usuario')
    comentarios: Mapped[List['Comentario']] = relationship(back_populates='usuario')

carrinho_produto = Table(
    'carrinho_produto',
    Base.metadata,
    Column('carrinho_id', ForeignKey('carrinho.id'), primary_key=True),
    Column('produto_id', ForeignKey('produto.id'), primary_key=True),
    Column('quantidade', Integer, nullable=False, default=1)
)

compra_produto = Table(
    'compra_produto',
    Base.metadata,
    Column('compra_id', ForeignKey('compra.id'), primary_key=True),
    Column('produto_id', ForeignKey('produto.id'), primary_key=True),
    Column('quantidade', Integer, nullable=False, default=1)
)

class Compra(Base):
    __tablename__ = 'compra'

    id: Mapped[int] = mapped_column(primary_key=True)
    descricao: Mapped[str] = mapped_column(String(150), nullable = False)
    data_criacao: Mapped[Date] =  mapped_column(Date, nullable = False)

    usuario_id: Mapped[int] = mapped_column(ForeignKey('usuario.id'))
    usuario: Mapped['Usuario'] = relationship(back_populates='compras')    
    produtos_compra: Mapped[List['Produto']] = relationship(secondary=compra_produto, back_populates='compras')
    

class Carrinho(Base):
    __tablename__ = 'carrinho'

    id: Mapped[int] = mapped_column(primary_key=True)
    usuario_id: Mapped[int] = mapped_column(ForeignKey('usuario.id'))
    usuario: Mapped['Usuario'] = relationship(back_populates='carrinho')
    produtos: Mapped[List['Produto']] = relationship(secondary=carrinho_produto, back_populates='carrinho')

class Produto(Base):
    __tablename__ = 'produto'

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(80), nullable = False)
    preco: Mapped[float] = mapped_column(Float, nullable = False)
    categoria: Mapped[str] = mapped_column(String(40), nullable = False)
    informacao: Mapped[str] = mapped_column(String(400), nullable = False)
    compras: Mapped[List['Compra']] = relationship(secondary=compra_produto, back_populates='produtos_compra')
    carrinho: Mapped[List['Carrinho']] = relationship(secondary=carrinho_produto, back_populates='produtos')
    comentarios: Mapped[List['Comentario']] = relationship(back_populates='produto')

class Comentario(Base):
    __tablename__ = 'comentario'
    id: Mapped[int] = mapped_column(primary_key=True)
    texto: Mapped[str] = mapped_column(String(500), nullable=False)
    autor: Mapped[str] = mapped_column(String(50), nullable=False)
    nota: Mapped[int] = mapped_column(nullable=False)

    usuario_id: Mapped[Optional[int]] = mapped_column(ForeignKey('usuario.id'), nullable=True)
    usuario: Mapped[Optional['Usuario']] = relationship(back_populates='comentarios')

    produto_id: Mapped[int] = mapped_column(ForeignKey('produto.id'), nullable=False)
    produto: Mapped['Produto'] = relationship(back_populates='comentarios')
