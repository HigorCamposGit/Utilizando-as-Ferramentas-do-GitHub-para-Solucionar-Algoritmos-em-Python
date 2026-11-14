"""
Desafio: Verificador de Número Par ou Ímpar
Objetivo: Ler números inteiros em sequência e permitir encerrar digitando 'sair'.
"""

def main():
    print("=== Verificador de Número Par ou Ímpar ===")
    print("Dica: Digite 'sair' a qualquer momento para encerrar o programa.\n")

    while True:
        # Recebe a entrada do usuário com o aviso direto no campo de digitação
        entrada_str = input("Digite um número inteiro (ou 'sair' para encerrar): ").strip()

        # Verifica se o usuário quer sair
        if entrada_str.lower() in ['sair', 's', 'exit', 'quit']:
            print("Encerrando o verificador. Até logo!")
            break

        try:
            # Converte para inteiro e verifica a paridade
            entrada = int(entrada_str)

            if entrada % 2 == 0:
                print(f"-> O número {entrada} é Par.\n")
            else:
                print(f"-> O número {entrada} é Ímpar.\n")
                
        except ValueError:
            print("-> Erro: Por favor, insira um número inteiro válido ou 'sair'.\n")

if __name__ == "__main__":
    main()
