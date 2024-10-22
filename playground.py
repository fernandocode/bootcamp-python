listObj = []

listObj.append((1, 10))
listObj.append((2, 20))
listObj.append((1, 30))
listObj.append((2, 40))

for key, value in listObj:
    print(f"{key} - {value}")
    # print(f"{item.tipo} - {item.valor}")
    
print("direita".rjust(15), "a")
print("esquerda".ljust(15), "a")