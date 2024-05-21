

arquivo = input("digite o nome do arquivo: ")
    
nome_arquivo = arquivo
with open(nome_arquivo, "w") as arquivo:   
   arquivo.write("oi")
print("frase salva com sucesso", frase)