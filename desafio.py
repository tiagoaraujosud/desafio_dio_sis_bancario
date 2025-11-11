menu_conta = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

menu_cliente = """

[a] Acessar Conta
[c] Criar Conta
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

clientes = {}
contas = {}

def deposito(extrato):

    valor = float(input("Informe o valor do depósito: "))
    
    if valor > 0:
        print("Depósito realizado!")
        extrato += f"Depósito: R$ {valor:.2f}\n"
        return valor, extrato
    else:
        print("Operação falhou! O valor informado é inválido.")

def sacar(saldo, limite, numero_saques, extrato):
    valor = float(input("Informe o valor do saque: "))
    
    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")
        
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, limite, numero_saques, extrato

def imprime_extrato(extrato, /, saldo):
    print("\n================ EXTRATO ================")
    if extrato == "":
        print("Não foram realizadas movimentações.\n" + extrato)
    else:
        print(extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_cliente():
    nome = str(input("Nome: "))
    data_nas = str(input("Data de Nascimento: "))
    cpf = str(input("CPF(Somente números): "))
    endereco = str(input("Endereço: "))

while True:
    
    opcao = input(menu_cliente)

    if opcao == "a":
        print("Acessou a conta")

    elif opcao == "c":
        print("Criou conta")
        
    elif opcao == "q":
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.") 
        
while True:
    
    opcao = input(menu_conta)

    if opcao == "d":
        novo_valor, novo_extrato = deposito(extrato)
        saldo += novo_valor
        extrato = novo_extrato

    elif opcao == "s":
        novo_saldo, conta_saques, novo_extrato = sacar(saldo=saldo, limite=limite, numero_saques=numero_saques, extrato=extrato)
        saldo = novo_saldo
        numero_saques = conta_saques
        extrato = novo_extrato

    elif opcao == "e":
        imprime_extrato(extrato, saldo=saldo)
        
    elif opcao == "c":
        criar_cliente()
        
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")