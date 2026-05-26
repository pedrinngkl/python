from flask import Flask, request, render_template_string

app = Flask(__name__)

def show_the_login_form():
    return render_template_string("""
        <h2>Login</h2>
        <form method="POST">
            <input type="text" name="usuario" placeholder="Usuário"><br><br>
            <input type="password" name="senha" placeholder="Senha"><br><br>
            <button type="submit">Entrar</button>
        </form>
    """)

def do_the_login():
    usuario_inserido = request.form.get('usuario')
    senha_inserida = request.form.get('senha')

    usuarios_permitidos = {
        "pedro": "22503161", 
        "dolga": "cotemig2026",
        "janaina": "cotemig2026",
        "antonio": "cotemig2026"
    }

    acesso_permitido = False
    for usuario, senha in usuarios_permitidos.items():
        if usuario == usuario_inserido and senha == senha_inserida:
            acesso_permitido = True
            break

    if acesso_permitido:
        return f"<h1>Bem-vindo, {usuario_inserido}!</h1>"
    else:
        return "<h1>Login inválido</h1>"

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

if __name__ == "__main__":
    app.run(debug=True)