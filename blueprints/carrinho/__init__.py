from flask import Blueprint

carrinho_bp = Blueprint("carrinho", __name__, template_folder="templates")

from blueprints.carrinho import routes
