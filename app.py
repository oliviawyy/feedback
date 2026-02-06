from flask import Flask, render_template, redirect, request

app = Flask(__name__)

app.secret_key = "banana"
lista_de_comentarios = []


@app.route("/")
def pagina_principal():
    return render_template("principal.html")

@app.route("/sobre")
def pagina_sobre():
    return render_template("sobre.html")

@app.route("/login", methods=["GET"])
def pagina_login():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login_post():
    email = request.form.get("email")
    senha = request.form.get("senha")

    if email == "oii@gmail.com" and senha == "1234":
        return redirect("/comentarios")
    else:
        return render_template("login.html", erro = "Acesso Negado!")

# PAGINA RESTRITA
@app.route("/comentarios")
def pagina_comentarios():
    return render_template("comentarios.html", lista_de_comentarios = lista_de_comentarios)

@app.route("/adicionar_comentario", methods = ["POST"])
def adicionar_comentario():
    comentario =  request.form.get("comentario")
    lista_de_comentarios.append(comentario)
    print(lista_de_comentarios)
    return redirect("/comentarios")

if __name__ == "__main__":
    app.run(host="0.0.0.0.", port=8080)


