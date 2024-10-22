print(True and True) # True
print(True and False) # False
print(False and False) # False
print(True or True) # True
print(True or False) # True
print(False or False) # False

saldo = 1000
saque = 200
limite = 100
conta_especial= True

exp = (saldo <= saque and saque <= limite) or (conta_especial and saldo >= saldo)
print(exp)

conta_normal_com_saldo_suficiente = (saldo <= saque and saque <= limite) 
conta_especial_com_saldo_suficiente = (conta_especial and saldo >= saldo)

exp2 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp2)