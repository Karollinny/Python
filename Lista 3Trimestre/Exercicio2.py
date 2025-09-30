def idade(numero):
    if (numero >= 18):
         print("O usuário é maior de idade", numero)
    else:
         print("O usuário não é maior de idade")

numero = int(input('Digite a sua idade:'))

idade(numero)