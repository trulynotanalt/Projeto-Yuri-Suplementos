from blueprints.compra import compra_bp
from flask import request, render_template, redirect, url_for, session
from services.compra_service import *
from services.carrinho_service import *
from services.produto_service import *

@compra_bp.route('/compra')
def compra():
    if 'usuario_id' not in session:
            flash('Você não está logado')
            return redirect(url_for('auth.login'))
    
    compras = listar_compra(session['usuario_id'])
    return render_template('compras.html', compras=compras)

@compra_bp.route('/compra/finalizar', methods=['GET','POST'])
def compra_adicionar():
    if 'usuario_id' not in session:
            flash('Você não está logado')
            return redirect(url_for('auth.login'))
    if request.method == 'POST':
        carrinho = listar_carrinho(session['usuario_id'])
        if not carrinho:
            flash('não tem produtos no carrinho')
        for produto, quantidade in carrinho:
            adicionar_compra(session['usuario_id'], produto.id, quantidade)
            remover_carrinho(session['usuario_id'], produto.id)
        flash('compra efetuada')
        return redirect(url_for('compra.compra'))

