"""
Desafio: Concatenação de Dados
Objetivo: Receber dois valores de entrada do usuário e combiná-los em uma única string de forma amigável.
"""

def main():
    # Recebe os dados de entrada com mensagens guia no terminal
    info1 = input("Digite o primeiro texto ou dado: ").strip()
    info2 = input("Digite o segundo texto ou dado: ").strip()

    # Concatena os valores garantindo espaçamento adequado
    resultado = f"{info1} {info2}"

    # Exibe o resultado formatado
    print("Resultado da concatenação:", resultado)

if __name__ == "__main__":
    main()
