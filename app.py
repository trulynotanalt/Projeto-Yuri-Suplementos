from flask import Flask
from blueprints.auth import auth_bp
app = Flask(__name__)
app.secret_key = "secret-peter"

app.register_blueprint(auth_bp)

if __name__ == "__main__":
    app.run(debug=True)

