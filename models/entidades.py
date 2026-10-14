from typing import List
from sqlalchemy import String, Float, ForeignKey, Table, Column
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class Usuario(Base):
    __tablename__ = 'usuario'

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(60), nullable = False)
    email: Mapped[str] = mapped_column(String(90), unique=True, nullable = False)
    senha_ou_hash: Mapped[str] = mapped_column(String(220), nullable = False)

    receitas: Mapped[List['Receita']] = relationship(back_populates='usuario')

receita_produto = Table(
    'receita_produto',
    Base.metadata,
    Column('receita_id', ForeignKey('receita.id'), primary_key=True),
    Column('produto_id', ForeignKey('produto.id'), primary_key=True)
)

class Receita(Base):
    __tablename__ = 'receita'

    id: Mapped[int] = mapped_column(primary_key=True)
    descricao: Mapped[str] = mapped_column(String(150), nullable = False)
    data_criacao: Mapped[str] = mapped_column(String(12), nullable = False)

    usuario_id: Mapped[int] = mapped_column(ForeignKey('usuario.id'))
    usuario: Mapped['Usuario'] = relationship(back_populates='receitas')
    produtos: Mapped[List['Produto']] = relationship(secondary=receita_produto, back_populates='receitas')

class Produto(Base):
    __tablename__ = 'produto'

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(80), nullable = False)
    preco: Mapped[float] = mapped_column(Float, nullable = False)
    informacao: Mapped[str] = mapped_column(String(90), nullable = False)

    receitas: Mapped[List['Receita']] = relationship(secondary=receita_produto, back_populates='produtos')

