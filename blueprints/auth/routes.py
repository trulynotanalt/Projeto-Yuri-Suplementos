from blueprints.auth import auth_bp
from flask import request, session, flash, redirect, render_template, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from services import user_service as service

@auth_bp('/auth/login', methods=['GET', 'POST'])
def login():
    if 'usuario_nome' in session or 'usuario_id' in session:
        flash('Você já está logado')
        return redirect(url_for('index'))
    
    if request.method == 'GET':
        return render_template('login.html')
    
    email = request.form.get('email')
    senha = request.form.get('senha')

    usuario = service.get_usuario_por_email(email=email)

    if usuario is None:
        flash('Email inválido')
        return render_template(redirect('login'))
    
    if (check_password_hash(usuario.senha_hash, senha)):
        session['usuario_nome'] = usuario.nome
        session['usuario_id'] = usuario.id

        return redirect(url_for('index', usuario=usuario))

@auth_bp('/auth/cadastro', methods=['GET', 'POST'])
def cadastro():
    if 'usuario_nome' in session or 'usuario_id' in session:
        flash('Você já possui uma conta')
        return redirect(url_for('index'))
    
    if request.method == 'GET':
        return render_template('cadastro.html')
    
    nome = request.form.get('nome')
    email = request.form.get('email')
    senha = request.form.get('senha')
    senha_hash = generate_password_hash(senha)

    usuario = service.create_usuario(nome=nome, email=email, senha_hash=senha_hash)

    if usuario is None:
        flash('Alguma informação está inválida')
        return render_template(redirect('cadastro'))
    
    session['usuario_nome'] = usuario.nome
    session['usuario_id'] = usuario.id

    return redirect(url_for('index', usuario=usuario))

@auth_bp('/auth/logout')
def logout():
    if 'usuario_id' not in session:
        flash('Você não está logado')
        return redirect(url_for('login'))

    session.pop('usuario_id')
    session.pop('usuario_nome')

    return redirect(url_for('index'))


      

    
    