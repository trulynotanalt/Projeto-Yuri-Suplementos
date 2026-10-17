from flask import Blueprint

produto_bp = Blueprint("produto", __name__, template_folder="templates")

from blueprints.produto import routes