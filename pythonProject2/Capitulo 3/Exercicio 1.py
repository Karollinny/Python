def right_justify(palavra, tamanhoPalavra):
     espaco = " " * (70-tamanhoPalavra)
     return espaco + palavra

# main
palavra = str(input("Digite uma palavra:"))
tamanhoPalavra = len(palavra)
right_justify(palavra, tamanhoPalavra)
justificado = right_justify(palavra, tamanhoPalavra)

print(justificado)
