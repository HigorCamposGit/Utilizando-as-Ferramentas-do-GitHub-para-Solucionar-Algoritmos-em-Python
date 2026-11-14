"""
Desafio: Concatenação de Dados
Objetivo: Unir múltiplos textos enviados pelo usuário de forma amigável.
"""

def main():
    print("=== Concatenação de Dados ===")
    
    info1 = input("Digite o primeiro texto ou dado: ").strip()
    info2 = input("Digite o segundo texto ou dado: ").strip()

    resultado = f"{info1} {info2}"

    print(f"-> Resultado da concatenação: {resultado}")

if __name__ == "__main__":
    main()
