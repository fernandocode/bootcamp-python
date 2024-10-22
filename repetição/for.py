texto = input("Informe um texto:")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()
    print("Executa no fim do for")
    
for numero in range(0, 11):
    print(numero, end=" ")

print()
    
for numero in range(0, 51, 5):
    print(numero, end=" ")