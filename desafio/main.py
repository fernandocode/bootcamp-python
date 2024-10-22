OPERACAO_DEPOSITO = "d"
OPERACAO_SAQUE = "s"
OPERACAO_EXTRATO = "e"
OPERACAO_SAIR = "q"

MSG_VALOR_INVALIDO = "Operação falhou! O valor informado é inválido."

VALOR_LIMITE_POR_SAQUE = 500
LIMITE_SAQUES = 3
saldo = 0
numero_saques = 0
transacoes = []

menu = f"""

[{OPERACAO_DEPOSITO}] Depositar
[{OPERACAO_SAQUE}] Sacar
[{OPERACAO_EXTRATO}] Extrato
[{OPERACAO_SAIR}] Sair

=> """

def decricao_operacao(operacao):
    if operacao == OPERACAO_DEPOSITO:
        return "Depósito"
    elif operacao == OPERACAO_SAQUE:
        return "Saque"
    
def format_valor_extrato(valor: float):
    return f"R$ {valor:.2f}".rjust(15)

def format_label_extrato(label: str):
    return f"{label}:".ljust(30)
    
def registar_deposito(valor: float):
    if valor > 0:
        global saldo
        saldo += valor
        transacoes.append((opcao, valor))
    else:
        print(MSG_VALOR_INVALIDO)
    
def registar_saque(valor: float):
    global saldo, numero_saques
    excedeu_saldo = valor > saldo
    excedeu_limite_por_saque = valor > VALOR_LIMITE_POR_SAQUE
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite_por_saque:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        transacoes.append((opcao, valor))
        numero_saques += 1
    else:
        print(MSG_VALOR_INVALIDO)
        
def gerar_extrato():
    if not transacoes:
        print("Não foram realizadas movimentações.")
    else:        
        print(" EXTRATO ".center(45, "="))
        print()
        for tipo, valor in transacoes:
            print(f"{format_label_extrato(decricao_operacao(tipo))}{format_valor_extrato(valor)}")
        print(f"\n{format_label_extrato("Saldo atual")}{format_valor_extrato(saldo)}\n")
        print("".center(45, "="))
    
def try_parse_numerico(valor_str: str):
    try:
        return float(valor_str)
    except:
        return 0

while True:
    opcao = input(menu)
    if opcao == OPERACAO_DEPOSITO:
        valor = try_parse_numerico(input("Informe o valor do depósito: "))
        registar_deposito(valor)
    elif opcao == OPERACAO_SAQUE:
        valor = try_parse_numerico(input("Informe o valor do saque: "))
        registar_saque(valor)
    elif opcao == OPERACAO_EXTRATO:
        gerar_extrato()
    elif opcao == OPERACAO_SAIR:
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")