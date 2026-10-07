from flask import Blueprint, render_template, session, redirect, url_for


controlador_conductor = Blueprint(
    "controlador_conductor",
    __name__
)


@controlador_conductor.route("/conductor")
def panel():

    if "id_usuario" not in session:
        return redirect(
            url_for("controlador_login.login")
        )

    if session.get("rol") != "Conductor":
        return redirect(
            url_for("controlador_login.login")
        )

    return render_template(
        "panel_conductor/index.html"
    )