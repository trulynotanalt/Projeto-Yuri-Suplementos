from blueprints.carrinho import carrinho_bp
from flask import request, render_template, redirect, url_for, session
from services.carrinho_service import *
from services.produto_service import *

@carrinho_bp.route('/carrinho')
def carrinho():
    carrinho = listar_carrinho(session['usuario_id'])
    return render_template('carrinho.html', carrinho=carrinho)

@carrinho_bp.route('/carrinho/adicionar/<int:id>', methods=['GET','POST'])
def carrinho_adicionar(id):
    if request.method == 'POST':
        adicionar_carrinho(session['usuario_id'], id)
        return redirect(url_for('carrinho.carrinho'))

@carrinho_bp.route('/carrinho/remover/<int:id>', methods=['GET','POST'])
def carrinho_remover(id):
    if request.method == 'POST':
        remover_carrinho(session['usuario_id'], id)
        return redirect(url_for('carrinho.carrinho'))