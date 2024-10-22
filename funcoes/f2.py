
def salvar_carro(modelo, ano, placa, /,  marca, *, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)
    
    
salvar_carro("EcoSport", 2020, "DFE23D3", "Ford", motor="1.6", combustivel="Gasolina")
salvar_carro("EcoSport", 2020, "DFE23D3", marca="Ford", motor="1.6", combustivel="Gasolina")

def somar(a,b):
    return a + b

def subtrair(a,b):
    return a - b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"Resultado de {a} + {b} = {resultado}")
    
exibir_resultado(10, 11, somar)
exibir_resultado(10, 11, subtrair)