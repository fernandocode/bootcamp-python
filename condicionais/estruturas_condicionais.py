MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas praticas")
else:
    print("Menor de idade")