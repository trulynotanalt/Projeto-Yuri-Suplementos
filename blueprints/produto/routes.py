from blueprints.produto import produto_bp
from flask import render_template, request, redirect, flash
from services import produto_service

@produto_bp.route('/loja', methods=['GET'])
def loja():
    nome = request.args.get('nome', '').strip()
    categoria = request.args.get('categoria', '').strip()

    if nome:
        produtos = produto_service.buscar_produtos_por_nome(nome)
    elif categoria:
        produtos = produto_service.buscar_produtos_por_categoria(categoria)
    else:
        produtos = produto_service.listar_todos_produtos()

    return render_template('loja.html', produtos=produtos)

@produto_bp.route('/loja/<int:id>', methods=['GET'])
def loja_detalhes(id):
    produto = produto_service.buscar_produto_por_id(id)

    if not produto:
       flash("Tal produto não existe")
       return redirect('produto.loja')

    return render_template('loja_detalhes.html', produto=produto)
