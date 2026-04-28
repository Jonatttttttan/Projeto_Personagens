from flask import render_template, request, redirect, flash, url_for, Blueprint
import os

import pandas as pd
import numpy as np
from datetime import datetime

from app.models.character import Character

from dotenv import load_dotenv

load_dotenv()

principal_bp = Blueprint("principal", __name__)

@principal_bp.route("/")
def home():

    return render_template("home.html")

@principal_bp.route("/index")
def index():
    characters = Character.query.all()
    return render_template("index.html", characters=characters)

@principal_bp.route("/adicionar", methods=["POST"])
def adicionar():
    nome = request.form.get("nome")
    descricao = request.form.get("descricao")

    if not nome or not descricao:
        flash("Preencha todos os campos!", "error")
        return redirect(url_for("principal.index"))

    # Criando objeto personagem
    novo_personagem = Character(
        nome = nome,
        descricao = descricao
    )

    from app import db
    db.session.add(novo_personagem)
    db.session.commit()

    flash("Personagem criado com sucesso!", "sucess")
    return redirect(url_for("principal.index"))



