def calculaTempo(distancia, velocidadeMedia):
     return distancia / velocidadeMedia

def calculaHora(TempoViagem):
    return TempoViagem // 3600


distancia = float(input("Digite a distancia"))
velocidadeMedia = float(input("Digite a velocidade"))

TempoViagem = calculaTempo(distancia, velocidadeMedia)
horaViagem = calculaHora(TempoViagem)


print("O tempo será de:", horaViagem)