# %%
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("Valor inválido para depósito.")
    return saldo, extrato

def sacar(saldo, valor, limite, numero_saques, extrato):
    if valor > saldo:
        print("Saldo insuficiente.")
    elif valor > limite:
        print("Valor acima do limite permitido.")
    elif numero_saques >= LIMITE_SAQUES:
        print("Número máximo de saques atingido.")
    else:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    print("\n=== Extrato ===")
    print(extrato if extrato else "Nenhuma movimentação realizada.")
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("================\n")

def obter_valor(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor < 0:
                raise ValueError("O valor não pode ser negativo.")
            return valor
        except ValueError as e:
            print(f"Entrada inválida: {e}")

def main():
    global saldo, extrato, numero_saques
    while True:
        opcao = input(menu).lower().strip()

        if opcao == "d":
            valor = obter_valor("Digite o valor do depósito: ")
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = obter_valor("Digite o valor do saque: ")
            saldo, extrato, numero_saques = sacar(saldo, valor, limite, numero_saques, extrato)

        elif opcao == "e":
            exibir_extrato(saldo, extrato)
        
        elif opcao == "q":
            print("Saindo...")
            break
        else:
            print("Opção inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()