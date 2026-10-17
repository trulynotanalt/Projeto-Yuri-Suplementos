from blueprints.user import user_bp
from flask import request, session, redirect, url_for, flash, render_template
from services import user_service as service

@user_bp.route('/usuario/perfil', methods=['GET'])
def me():
    if 'usuario_id' not in session:
        flash('Você não está logado')
        return redirect(url_for('login'))

    usuario = service.get_usuario(int(session.get('usuario_id')))

    return render_template('perfil_usuario.html', usuario=usuario)

@user_bp.route('usuario/editar', methods=['GET', 'POST'])
def usuario_editar():
    if 'usuario_id' not in session:
        flash('Você não está logado')
        return redirect(url_for('login'))
    
    if request.method == 'GET':
        usuario = service.get_usuario(int(session.get('usuario_id')))
        return render_template('editar_usuario.html', usuario=usuario)

    nome = request.form.get('nome')
    email = request.form.get('nome')

    service.update_usuario(int(session.get('usuario_id')), nome=nome, email=email)

    return redirect(url_for('usuario_perfil'))

@user_bp.route('usuario/excluir', methods=['GET', 'POST'])
def usuario_excluir():
    if 'usuario_id' not in session:
        flash('Você não está logado')
        return redirect(url_for('login'))
    
    if request.method == 'GET':
        return render_template('excluir_usuario.html')

    if not service.delete_usuario(int(session.get('usuario_id'))):
        flash('O usuário não foi excluído')
        return redirect(url_for('index'))

    session.pop('usuario_id', None)
    session.pop('usuario_nome', None)

    return redirect(url_for('index'))
