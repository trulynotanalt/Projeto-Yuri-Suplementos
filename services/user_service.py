from models import Usuario
from sqlalchemy import select
from database import nova_sessao


def get_usuario(id):

    with nova_sessao() as session:
        statement = select(Usuario).where(Usuario.id == id)
        user =  session.scalars(statement).first()

    return  user

def get_usuario_por_email(email):
    with nova_sessao() as session:
        statement = select(Usuario).where(Usuario.email == email)
        user =  session.scalars(statement).first()
        
    return user

def create_usuario( nome, email, senha_hash):
    with nova_sessao() as session:
        usuario =  Usuario(
            nome = nome,
            email = email,
            senha_hash = senha_hash,
        )

        session.add(usuario)
        session.commit()

        session.refresh(usuario)

    return usuario


def update_usuario(id, nome = None, email = None):
    usuario = get_usuario(id)

    if usuario is None:
        return None

    if nome is not None:
        usuario.nome = nome

    if email is not None:
        usuario.email = email

    with nova_sessao() as session:
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

