import random

def menu():
    print("\n===== SIMULADOR DE CARTÃO DE CRÉDITO =====")
    print("1. Validar número de cartão")
    print("2. Gerar cartão de crédito válido")
    print("3. Sair")
    opcao = input("Escolha uma opção: ")
    return opcao

def luhn_valido(numero):
    soma = 0
    alternar = False
    for digito in reversed(numero):
        n = int(digito)
        if alternar:
            n *= 2
            if n > 9:
                n -= 9
        soma += n
        alternar = not alternar
    return soma % 10 == 0

def validar_cartao():
    numero = input("Digite o número do cartão (sem espaços ou traços): ")
    if not numero.isdigit():
        print("Erro: O número deve conter apenas dígitos!")
        return
    
    if luhn_valido(numero):
        print(" Número válido ")
    else:
        print(" Número inválido")

def gerar_cartao_valido():
    
    base = ''.join([str(random.randint(0, 9)) for _ in range(15)])
    
    soma = 0
    alternar = True  
    for digito in reversed(base):
        n = int(digito)
        if alternar:
            n *= 2
            if n > 9:
                n -= 9
        soma += n
        alternar = not alternar
    
    digito_verificador = (10 - (soma % 10)) % 10
    numero_completo = base + str(digito_verificador)
    
    numero_formatado = ' '.join([numero_completo[i:i+4] for i in range(0, 16, 4)])
    print(f"Cartão gerado: {numero_formatado}")

def main():
    while True:
        opcao = menu()
        if opcao == '1':
            validar_cartao()
        elif opcao == '2':
            gerar_cartao_valido()
        elif opcao == '3':
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha 1, 2 ou 3.")

if __name__ == "__main__":
    main()
