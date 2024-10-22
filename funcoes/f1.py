def exibir_mensagem():
    print("Olá mundo!")
    
def exibir_mensagem_2(nome):
    print(f"Sejá bem vindo {nome}!")
    
def exibir_mensagem_3(nome = "Anonimo"):
    print(f"Sejá bem vindo {nome}!")
    
exibir_mensagem()
exibir_mensagem_2("Fernando")
exibir_mensagem_3()

def calcular_total(valores):
    return sum(valores)

def retornar_antecessor_e_sucessor(numero):
    antecessor = numero - 1 
    sucessor = numero + 1 
    return antecessor, sucessor

def func_r_none():
    print("Não retorna nada")

print(calcular_total([10,20,34]))
print(retornar_antecessor_e_sucessor(10))
print(func_r_none())

def salvar_carro(marca, modelo, placa, ano):
    print(f"Carro inserido com sucesso {marca}/{modelo}/{placa}/{ano}")
    
salvar_carro("Ford", "EcoSport", "DFE23D3", 2020)
salvar_carro(marca="Ford", modelo="EcoSport", placa="DFE23D3", ano=2020)
salvar_carro(**{"marca":"Ford", "modelo":"EcoSport", "placa":"DFE23D3", "ano":2020})

#args
def salvar_carro_args(*carro):
    print(f"Carro inserido com sucesso {carro.marca}/{carro.modelo}/{carro.placa}/{carro.ano}")
    
#kwargs
def salvar_carro_kwargs(**carro):
    print(f"Carro inserido com sucesso {carro.marca}/{carro.modelo}/{carro.placa}/{carro.ano}")  

def texto(title, *body, **footer):
    print(body)
    print(footer)
    footer_str = "\n".join([f"{chave.title()}: {valor}" for chave, valor in footer.items()])
    print(f"{title}\n\n{"\n".join(body)}\n\n{footer_str}")
    
salvar_carro(marca="Ford", modelo="EcoSport", placa="DFE23D3", ano=2020)
salvar_carro(**{"marca":"Ford", "modelo":"EcoSport", "placa":"DFE23D3", "ano":2020})
texto("Titulo!",
      "Item 1",
      "Item 2",
      "Item 3",
      "Item 4",
      "Item 5",
      "Item 6",
      "Item 7",
      "Item 8",
      autor="Fernando",
      ano= 2012
      )