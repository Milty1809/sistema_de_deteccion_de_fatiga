from flask import Blueprint, render_template, request, session, redirect, url_for

from conexion import obtener_conexion


controlador_login = Blueprint(
    "controlador_login",
    __name__
)


@controlador_login.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        usuario = request.form.get("usuario")
        password = request.form.get("password")

        conexion = obtener_conexion()

        usuario_bd = conexion.execute("""
            SELECT *
            FROM usuario
            WHERE usuario = ?
            AND contraseña = ?
        """, (usuario, password)).fetchone()

        conexion.close()

        if usuario_bd:

            session["id_usuario"] = usuario_bd["id_usuario"]
            session["usuario"] = usuario_bd["usuario"]
            session["rol"] = usuario_bd["rol"]

            if usuario_bd["rol"] == "Admin":

                return redirect(
                    url_for("controlador_admin.panel")
                )

            if usuario_bd["rol"] == "Operador":

                return redirect(
                    url_for("controlador_operador.panel")
                )

            if usuario_bd["rol"] == "Conductor":

                return redirect(
                    url_for("controlador_conductor.panel")
                )

        return render_template(
            "inicio_de_sesion/index.html",
            error="Usuario o contraseña incorrectos."
        )

    return render_template(
        "inicio_de_sesion/index.html"
    )