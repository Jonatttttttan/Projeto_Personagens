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

# Index
@principal_bp.route("/index")
def index():
    characters = Character.query.all()
    print(f"Tipo de 'character': {type(characters)}")
    return render_template("index.html", characters=characters)

# Adicionar
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

# Deletar
@principal_bp.route("/deletar/<int:id>", methods=["POST"])
def delete(id):
    from app import db
    from app.models.character import Character

    personagem = Character.query.get_or_404(id)

    db.session.delete(personagem)
    db.session.commit()

    flash("Personagem removido com sucesso!", "success")
    return redirect(url_for("principal.index"))

@principal_bp.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    from app import db
    from app.models.character import Character

    personagem = Character.query.get_or_404(id)

    if request.method == "POST":
        personagem.nome = request.form.get("nome")
        personagem.descricao = request.form.get("descricao")

        db.session.commit()

        flash("Personagem atualizado com sucesso!", "success")
        return redirect(url_for("principal.index"))

    return render_template("editar.html", personagem=personagem)


