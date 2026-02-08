from flask import Flask, render_template, redirect, url_for, request

import bcrypt
from supabase_service import supabase

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():

    global current_user
    if request.method == 'POST':

        email = request.form.get("email")
        senha = request.form.get("senha").encode("utf-8")

        result = supabase.table('usuarios').select("*").eq("email", email).execute()
        if result.data:
            senha_hash = result.data[0]["senha"].encode("utf-8")
            if bcrypt.checkpw(senha, senha_hash):
                current_user = email
                return redirect(url_for("materiais"))
            else:
                print("erro")
    return render_template("login.html")

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == 'POST':
        nome = request.form.get('nome')
        nome_usuario = request.form.get('nick')
        email = request.form.get('email')
        senha = request.form.get('senha')

        senha_hash = bcrypt.hashpw(
            senha.encode('utf-8'),
            bcrypt.gensalt()
        ).decode('utf-8')

        exists = supabase.table("usuarios") \
            .select("*") \
            .eq("email", email) \
            .execute()

        if exists.data:
            return "Email já cadastrado"
        else:
            supabase.table("usuarios").insert({
                "nome": nome,
                "nome_usuario": nome_usuario,
                "email": email,
                "senha": senha_hash
            }).execute()

            return redirect(url_for("login"))

    return render_template("cadastro.html")

@app.route("/materiais")
def materiais():
    return render_template("materiais.html")

@app.route("/materia/fisica")
def fisica():
    return render_template("fisica.html")

@app.route("/materia/matematica")
def matematica():
    return render_template("matematica.html")

@app.route("/exercicios")
def exercicios():
    return render_template("exercicios.html")

# 👉 ROTA DE SAIR (LOGOUT)
@app.route("/logout")
def logout():
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
