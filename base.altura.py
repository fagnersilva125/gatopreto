def calcularcircunferencia(base):
    altura = input("digite a altura:")
    return int(base) * int(altura) / 2

if __name__ == "__main__":
    print(calcularcircunferencia(float(input("digite a base: "))))