'''Crie uma aplicação Flask que contenha uma rota específica responsável por explicar o conceito de decorator em Python.
Requisitos
Crie uma rota acessível por meio do caminho: /decorator
Ao acessar essa rota no navegador, deve ser exibido um texto explicando:
O que é um decorator em Python
Para que ele serve
Como ele é utilizado no Flask (exemplo: @app.route)'''

from flask import Flask

app = Flask(__name__)

@app.route('/decorator')
def explain_decorator():
    explanation =  """
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <style>
            body { font-family: sans-serif; line-height: 1.6; max-width: 800px; margin: 40px auto; padding: 20px; background-color: #f4f4f9; color: #333; }
            h1 { color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px; }
            .card { background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
            code { background: #e74c3c; color: white; padding: 2px 5px; border-radius: 4px; font-weight: bold; }
            .highlight { color: #2980b9; font-weight: bold; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>O que é um Decorator?</h1>
            <p>Um <strong>decorator</strong> em Python é uma função que recebe outra função como argumento e retorna uma nova função que geralmente estende ou modifica o comportamento da função original.</p>
            
            <p>Ele é usado para adicionar funcionalidades a funções existentes de forma <span class="highlight">elegante e reutilizável</span>, sem modificar o código da função original.</p>

            <h2>Decorators no Flask</h2>
            <p>No Flask, eles são amplamente utilizados para mapear rotas. Por exemplo, o decorator <code>@app.route</code> associa uma URL a uma função específica.</p>
            
            <p>Isso permite definir as rotas do seu aplicativo web e organizar o código de forma clara e eficiente!</p>
        </div>
    </body>
    </html>
    """
    return explanation

if __name__ == '__main__':
    app.run(debug=True)