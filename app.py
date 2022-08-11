from flask import Flask, render_template

app = Flask("projeto")

@app.route("/")
def ola_mundo():
    nome = "Alex Moura"
    produtos = [
        {"nome": "tomate", "preco": "12,99"},
        {"nome": "valorant points", "preco": "42,90"}
    ]
    return render_template("jinga2.html", n = nome, p = produtos), 200

app.run()