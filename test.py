
notaA=float(input("informe a primeira nota: "))
notaB=float(input("informe a segundsa nota: "))
notac=float(input("informe a terceira nota: "))

#calcular media
mediafinal = (notaA + notaB + notac) /3

#verificaçao
if mediafinal >=7.0:
   print("A MEDIA: %.1f - APROVADO"% mediafinal )
   
else:
    print("A MEDIA: %.1f - REPROVADO"% mediafinal)
    