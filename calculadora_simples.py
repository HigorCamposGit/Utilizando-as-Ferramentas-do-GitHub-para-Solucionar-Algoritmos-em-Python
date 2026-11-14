"""
Desafio: Calculadora Simples em Python
Objetivo: Realizar operações aritméticas básicas com base na entrada do usuário.
"""

def main():
    print("=== Calculadora Simples ===")
    
    try:
        num1 = float(input("Digite o primeiro número: ").strip())
        num2 = float(input("Digite o segundo número: ").strip())
        operador = input("Escolha a operação (+, -, *, /): ").strip()

        if operador == '+':
            resultado = num1 + num2
            print(f"-> Resultado: {num1} + {num2} = {resultado}")
        elif operador == '-':
            resultado = num1 - num2
            print(f"-> Resultado: {num1} - {num2} = {resultado}")
        elif operador == '*':
            resultado = num1 * num2
            print(f"-> Resultado: {num1} * {num2} = {resultado}")
        elif operador == '/':
            if num2 != 0:
                resultado = num1 / num2
                print(f"-> Resultado: {num1} / {num2} = {resultado}")
            else:
                print("-> Erro: Divisão por zero não é permitida.")
        else:
            print("-> Erro: Operador aritmético inválido.")
            
    except ValueError:
        print("-> Erro: Entrada numérica inválida. Por favor, insira números válidos.")

if __name__ == "__main__":
    main()
