print ("Calculadora cientifica")

while True:
    print ("1.Sumar")
    print ("2.Restar")
    print ("3.Multiplicar")
    print ("4.Dividir")
    print ("5.Left")

    opcion = input ("Ingresa una opcion")

    if opcion == "5":
        print ("¡Gracias por usar la calculadora! Bye!!")
        break 


    if opcion in ["1","2","3","4"]:
    
        num1 = float(input("Ingrese el primer numero:"))
        num2 = float(input("Ingresa el segundo numero:"))

        if opcion =="1":
            resultado = num1 + num2
            print(f"El resultado de la suma es :{num1} + {num2} = {resultado}")
        elif opcion == "2":
            resultado = num1 - num2 
            print(f"El resultado de la resta es:{num1} - {num2} = {resultado}") 
        elif opcion == "3": 
            resultado = num1 * num2
            print(f"El resultado de la multiplicacion es: {num1} * {num2} = {resultado}")
        elif opcion =="4":
            if num2 != 0:
                resultado = num1 / num2
                print (f"El resultado de la division es: {num1} / {num2} ={resultado}")
            else: 
                print("Error: No se puede dividir entre cero")
else:
    print("Opcion no valida. Intentelo de nuevo.")