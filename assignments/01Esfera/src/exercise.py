import math
def main():
    #escribe tu código abajo de esta línea
    print("Este programa calcula el área y volumen de una esfera")

    radio = float(input("Dame el valor del radio: "))

    area = 4 * math.pi * math.pow(radio,2)
    volumen = (4/3) * math.pi * math.pow(radio,3)

    print (f"El area es: {area}")
    print (f"El volumen es: {volumen}")
    
if __name__=='__main__':
    main()
