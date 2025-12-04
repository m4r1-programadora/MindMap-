from flask import Flask, render_template

app = Flask(__name__)

# Rota da página principal
@app.route("/")
def index():
    return render_template("index.html")

# Página de login
@app.route("/login")
def login():
    return render_template("login.html")

# Página de cadastro
@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")


# Executar o servidor
if __name__ == "__main__":
    app.run(debug=True)
