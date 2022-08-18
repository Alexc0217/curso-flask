from flask import Flask, render_template, request, session, redirect, url_for

app = Flask("projeto")
app.secret_key = "ASFAFQER#r#@r@#$r%$t@$gtgdfadfadfeaf"

@app.route("/")
def ola_mundo():
    nome = "Alex Moura"
    produtos = [
        {"nome": "tomate", "preco": "12,99"},
        {"nome": "valorant points", "preco": "42,90"}
    ]
    return render_template("jinga2.html", n = nome, p = produtos), 200

@app.route("/teste")
@app.route("/teste/<variavel>")
def funcao_teste(variavel = ""):
    return "nova rota teste <br> variavel: {}".format(variavel), 200

@app.route("/form")
def form():
    return render_template("form.html"), 200

@app.route("/form_recebe", methods = ["GET", "POST"])
def form_recebe():
    nome = ""
    if request.method == "POST":
        nome = request.form["nome"]
        return "Nome: {}".format(nome), 200
    else:
        return "Não pode chamar direto no GET.", 200

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/user-login", methods=["POST"])
def user():
    if request.form["usuario"] == "alexc" and request.form["senha"] == "2222":
        session["usuario"] = request.form["usuario"]
        session["codigo"] = 1
        return redirect(url_for("acesso_restrito"))
    else:
        return "Usuário/senha inválidos, digite novamente. ", 400

@app.route("/restrito")
def acesso_restrito():
    if(session["codigo"] == 1):
        return "Bem-vindo à área restrita!! <br/>Usuário: {} <br/>Código: {}".format(session["usuario"], session["codigo"])
    else:
        return "Acesso inválido. ", 400

app.run()