from flask import Blueprint, render_template, session, redirect, url_for


controlador_operador = Blueprint(
    "controlador_operador",
    __name__
)


@controlador_operador.route("/operador")
def panel():

    if "id_usuario" not in session:
        return redirect(
            url_for("controlador_login.login")
        )

    if session.get("rol") != "Operador":
        return redirect(
            url_for("controlador_login.login")
        )

    return render_template(
        "panel_operador/index.html"
    )