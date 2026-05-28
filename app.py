from flask import Flask, render_template, request, redirect
import models

app = Flask(__name__)

@app.route("/")
def index():
    usuarios = models.get_all_users()
    return render_template("index.html", usuarios=usuarios)

@app.route("/criar", methods=["GET", "POST"])
def criar():
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        models.create_user(nome, email)
        return redirect("/")
    return render_template("criar.html")

@app.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        models.update_user(id, nome, email)
        return redirect("/")

    usuario = models.get_user(id)
    return render_template("editar.html", usuario=usuario)

@app.route("/deletar/<int:id>")
def deletar(id):
    models.delete_user(id)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)