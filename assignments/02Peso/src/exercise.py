def main():
    #escribe tu código abajo de esta línea
    peso1= int(input("cual es el peso inicial"))
    peso2= int(input("cual es el peso final"))
    meses= int(input("cantidad de meses en bajar el peso"))
    pesoFinal= float((peso1 - peso2)/meses)
    print("tienes que bajar esta cantidad de kilos o libras por mes" + str(pesoFinal))


if __name__ == '__main__':
    main()
