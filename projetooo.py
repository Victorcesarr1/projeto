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