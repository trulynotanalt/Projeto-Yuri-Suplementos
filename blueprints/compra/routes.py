from blueprints.compra import compra_bp
from flask import request, render_template, redirect, url_for, session
from services.compra_service import *
from services.carrinho_service import *
from services.produto_service import *

@compra_bp.route('/compra')
def compra():
    compra = listar_compra(session['usuario_id'])
    return render_template('compra.html', compra=compra)

@compra_bp.route('/compra/comprar/<int:id>', methods=['GET','POST'])
def compra_adicionar(id):
    if request.method == 'POST':
        adicionar_compra(session['usuario_id'], id)
        remover_carrinho(session['usuario_id'], id)
        return redirect(url_for('compra.compra'))

@compra_bp.route('/compra/remover/<int:id>', methods=['GET','POST'])
def compra_remover(id):
    if request.method == 'POST':
        remover_compra(session['usuario_id'], id)
        return redirect(url_for('compra.compra'))