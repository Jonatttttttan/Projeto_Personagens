from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.user import User
from app import db
from flask_login import login_user, logout_user, login_required

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(username=username, password=password).first()

        if user:
            login_user(user)
            return redirect(url_for("principal.index"))
        else:
            flash("Credenciais inválidas")
    return render_template("login.html")

@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))

