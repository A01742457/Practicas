import math
def main():
    #escribe tu código abajo de esta línea
    print("Este programa calcula el área de un triángulo")

    a=float(input("Dame el valor de a: "))
    b=float(input("Dame el valor de b: "))
    c=float(input("Dame el valor de c: "))

    s= (a + b + c) / 2
    area = math.sqrt(s * (s-a) * (s-b) * (s-c))

    print (f"El area del triangulo es: {area}")



   
if __name__=='__main__':
    main()
