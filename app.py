from flask import Flask, render_template

from Backend.controlador.controlador_login import controlador_login
from Backend.controlador.controlador_admin import controlador_admin
from Backend.controlador.controlador_operador import controlador_operador
from Backend.controlador.controlador_conductor import controlador_conductor

app = Flask(__name__)

app.secret_key = "clave_secreta"

app.register_blueprint(controlador_login)
app.register_blueprint(controlador_admin)
app.register_blueprint(controlador_operador)
app.register_blueprint(controlador_conductor)

@app.route("/")
def home():
    return render_template("inicio_de_sesion/index.html")


if __name__ == "__main__":
    app.run(debug=True)