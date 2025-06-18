def calculaDiametro(raio):
     return 2 * raio

def calculaCircunferencia(pi, raio):
     return pi * raio * 2

def calculaAreaCircunferencia(pi, raio):
     return pi * (raio ** 2)

#Main
raio = float(input("Digite o valr do raio:"))

pi = 3.14159

diametro = calculaDiametro(raio)
circunferencia = calculaCircunferencia(pi, raio)
area = calculaAreaCircunferencia(pi, raio)

print("O diametro é de : ", diametro)
print("A circunferencia é de : ", circunferencia)
print("A area é de : ", area)