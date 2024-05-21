def maiuscula(frase):
    frase = frase[0].upper[] + frase[1: ]
    return frase, len(frase)

if __name__ == "__main__":
    frase = input("digite aqui: ")
    frase_maiscula, tamanho = maiuscula(frase)
    print("o tamanho da frase é: {}".format(tamanho))
    print(frase_maiscula)