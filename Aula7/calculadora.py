import math
from flask import render_template, request

def calcular():
    try:
        num1_valor = request.form.get("num1")
        if not num1_valor:
            return render_template("calculadora.html", etapas="Informe o primeiro número.", resultados="")
        
        num1 = float(num1_valor)
        operacao = request.form.get("operacao")

        if operacao == "sqrt":
            if num1 < 0:
                resultado = "Erro: número negativo"
                etapas = f"Não existe raiz real de {num1}."
            else:
                resultado = math.sqrt(num1)
                etapas = f"√{num1} = {resultado}"
            return render_template("calculadora.html", etapas=etapas, resultados=resultado)
        
        if operacao == "log":
            if num1 <= 0:
                resultado = "Erro: valor inválido"
                etapas = f"O logaritmo requer um número maior que zero."
            else:
                resultado = math.log10(num1)
                etapas = f"log10({num1}) = {resultado}"
            return render_template("calculadora.html", etapas=etapas, resultados=resultado)

        num2_valor = request.form.get("num2", "").strip()
        if not num2_valor:
            return render_template("calculadora.html", etapas="Informe o segundo número para esta operação.", resultados="")

        num2 = float(num2_valor)

        if operacao == "+":
            resultado = num1 + num2
            etapas = f"{num1} + {num2} = {resultado}"
        elif operacao == "-":
            resultado = num1 - num2
            etapas = f"{num1} - {num2} = {resultado}"
        elif operacao == "*":
            resultado = num1 * num2
            etapas = f"{num1} * {num2} = {resultado}"
        elif operacao == "/":
            if num2 == 0:
                resultado = "Erro: divisão por zero"
                etapas = "Não é possível dividir por zero."
            else:
                resultado = num1 / num2
                etapas = f"{num1} / {num2} = {resultado}"
        elif operacao == "**":
            resultado = num1 ** num2
            etapas = f"{num1} ^ {num2} = {resultado}"
        else:
            return render_template("calculadora.html", etapas="Operação inválida.", resultados="")

        return render_template("calculadora.html", etapas=etapas, resultados=resultado)

    except ValueError:
        return render_template("calculadora.html", etapas="Por favor, insira valores numéricos válidos.", resultados="")
