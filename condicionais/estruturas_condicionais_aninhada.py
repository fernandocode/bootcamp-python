conta_normal = False
conta_universitaria = False

saldo = 2000
saque = 2500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Realizado")
    elif saque <= (saldo + cheque_especial):
        print("Realizado com saldo especial")
    else:
        print("Saldo insuficiente")

if conta_universitaria:
    if saldo >= saque:
        print("Realizado")
    else:
        print("Saldo insuficiente")
        
else:
    print("Não reconhecido")