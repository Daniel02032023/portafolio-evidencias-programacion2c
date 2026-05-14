#funciones basicas
def suma (a,b):
    result = a+b
    return result

def resta(a,b) :
    result = a-b
    return result

def multi(a,b):
    result = a*b
    return result 

def div(a,b):
    return a/b

#menu de opciones
opcion =0
while(opcion !=5):
    print("----menu de opciones----")
    print("1.sumar 2 valores")
    print("2.restar 2 valores")
    print("3.multiplicar 2 valores")
    print("4.Dividir 2 valores")
    print("5.terminar ptograma")
    opcion =int(input("\inSeleccionar la opcion deseada [1-5:] "))

if opcion == 1:
    #suma de dos numeros
    n1 = float(input("\inIngresa el primer numero a sumar: "))
    n2 = float(input("\inIngresa el segundo numero a sumar "))
    print(f"diferencia de la suma: {suma(n1,n2)}")
elif opcion ==2 :
    #resta de dos numeros
    n1 = float(input("\inIngresa el minuendo: "))
    n2 = float(input("\inIngresa el sustreando: "))
    print(f"cociente de la resta: {resta(n1,n2)}")
elif opcion == 3 :
    #multiplicacion de dos numeros
   n1 = float(input("\inIngresa el primer factor: "))
   n2 = float(input("\inIngresa el segundo factor: "))
   print(f"producto resultante: {multi(n1,n2)}")
elif opcion == 4 :
    #divicion de dos numeros
   n1 = float(input("\inIngresa el minuendo: "))
   n2 = float(input("\inIngresa el divisor: "))
   print(f"cociente resultante: {div(n1,n2)}")
elif opcion == 5 :
    #finaliza el programa
    print("programa finalizado...")


else:
    #mensaje de error por opcion na valida
    print("opcion seleccionado na valida,intentar nueva mente!")