num_1= float(input("primer numero a consultar: "))
num_2= float(input("segundo numero a consultar: "))
operador = input("que operacion vs a hacer?(+,-,/,*): ")

if operador == "+":
    print("Resultado", num_1 + num_2)
elif operador == "-":
    print("Resultado", num_1 - num_2)
elif operador == "*":
    print("Resultado", num_1 * num_2)
elif operador == "/":
    if num_2 != 0:
     print("Resultado", num_1 / num_2)
    else:
     print("Error dividiendo por cero.")
else:
    print("Operacion no valida")  


            
        