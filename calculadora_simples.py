"""
Desafio: Calculadora Simples em Python
Objetivo: Realizar operações aritméticas fundamentais com base nas entradas do usuário.
"""

def main():
    try:
        # Coleta os operandos e o operador aritmético com mensagens visíveis
        num1 = float(input("Digite o primeiro número: ").strip())
        num2 = float(input("Digite o segundo número: ").strip())
        operador = input("Escolha a operação (+, -, *, /): ").strip()

        # Executa a operação correspondente com tratamento de exceções lógicas
        if operador == '+':
            resultado = num1 + num2
            print(f"Resultado: {resultado}")
        elif operador == '-':
            resultado = num1 - num2
            print(f"Resultado: {resultado}")
        elif operador == '*':
            resultado = num1 * num2
            print(f"Resultado: {resultado}")
        elif operador == '/':
            if num2 != 0:
                resultado = num1 / num2
                print(f"Resultado: {resultado}")
            else:
                print("Erro: Divisão por zero não é permitida.")
        else:
            print("Erro: Operador aritmético inválido.")
            
    except ValueError:
        print("Erro: Entrada numérica inválida.")

if __name__ == "__main__":
    main()
