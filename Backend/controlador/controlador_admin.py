from flask import Blueprint, render_template, session, redirect, url_for

controlador_admin = Blueprint(
    "controlador_admin",
    __name__
)


@controlador_admin.route("/admin")
def panel():

    if "id_usuario" not in session:
        return redirect(
            url_for("controlador_login.login")
        )

    if session.get("rol") != "Admin":
        return redirect(
            url_for("controlador_login.login")
        )

    return render_template(
        "panel_admin/index.html"
    )