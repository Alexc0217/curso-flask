from flask import Flask

app = Flask("projeto")

@app.route("/")
def ola_mundo():

    return "Olá Mundo! Esse é meu primeiro projeto Flask!"

app.run()