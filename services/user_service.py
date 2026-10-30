from models import Usuario, Compra
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from database import nova_sessao
from services.result import Result
from sqlalchemy.exc import IntegrityError


def get_usuario(id):

    with nova_sessao() as session:
        statement = select(Usuario).where(Usuario.id == id).options(selectinload(Usuario.compras).selectinload(Compra.produtos_compra))
        user =  session.scalars(statement).first()

    return user

def get_usuario_por_email(email):
    with nova_sessao() as session:
        statement = select(Usuario).where(Usuario.email == email)
        user =  session.scalars(statement).first()
        
    return user

def create_usuario( nome, email, senha_hash):
    try:
        with nova_sessao() as session:
            usuario =  Usuario(
                nome = nome,
                email = email,
                senha_hash = senha_hash,
            )
            session.add(usuario)
            session.commit()
            session.refresh(usuario)

    except IntegrityError as error:
        session.rollback()
        if "UNIQUE constraint failed" in str(error):
            result = Result(False, "Já existe uma conta com alguma destas Informações")
            return result

        result = Result(False, "Ocorreu um erro, tente novamente", None)

    result = Result(True, None, usuario)
    return result


def update_usuario(id, nome = None, email = None):
    with nova_sessao() as session:
        statement = select(Usuario).where(Usuario.id == id)
        usuario = session.scalars(statement).first()

        if usuario is None:
            return None
        
        if nome is not None:
            usuario.nome = nome
    
        if email is not None:
            usuario.email = email
        
        session.commit()
        session.refresh(usuario)
    
    return usuario


def delete_usuario(id):
    usuario = get_usuario(id)
    
    if usuario is None:
        return False
    with nova_sessao() as session:
        session.delete(usuario)
        session.commit()

    return True

