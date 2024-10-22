def sacar(valor):
    saldo = 500
    if saldo >= valor:
        print("valor sacado!")
        print("retire seu dinheiro")
    print("Obrigado")
    
def depositar(valor):
    saldo = 500
    saldo += valor
        
sacar(1000)