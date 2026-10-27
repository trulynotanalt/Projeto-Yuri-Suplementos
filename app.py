from flask import Flask, render_template, session, url_for
from services import produto_service
from services.imagens_produtos import imagem_do_produto
from blueprints.auth import auth_bp
from blueprints.carrinho import carrinho_bp
from blueprints.compra import compra_bp
from blueprints.produto import produto_bp
from blueprints.user import user_bp
app = Flask(__name__)
app.secret_key = "secret-peter"

app.register_blueprint(auth_bp)
app.register_blueprint(carrinho_bp)
app.register_blueprint(compra_bp)
app.register_blueprint(produto_bp)
app.register_blueprint(user_bp)


@app.template_global()
def imagem_produto_url(produto):
    
    arquivo = imagem_do_produto(produto)
    if arquivo:
        return url_for('static', filename=f'img/produtos/{arquivo}')
    else: None


if __name__ == "__main__":
    app.run(debug=True)

@app.route('/')
def index():
    sugestoes = produto_service.listar_sugestoes()
    comprados = []
    if 'usuario_id' in session:
        comprados = produto_service.listar_produtos_comprados(session['usuario_id'])
    return render_template('index.html', sugestoes=sugestoes, produtos_comprados=comprados)