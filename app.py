from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/cadastro")
def cadastro():
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
