from blueprints.carrinho import carrinho_bp
from flask import request, render_template, redirect, url_for, session
from services.carrinho_service import *

@carrinho_bp.route('/carrinho')
def carrinho():
    carrinho = listar_carrinho(session['usuario_id'])
    return render_template('carrinho.html', carrinho=carrinho)
