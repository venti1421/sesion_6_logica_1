#iImplementar un acalculador aque pida dos numero y una operacion vamos a usar la figura de switch...case y luego con if... elif... else....  
#calculadora basica:

num_1= float(input("primer numero a consultar: "))
num_2= float(input("segundo numero a consultar: "))
operador = input("que operacion vs a hacer?(+,-,/,*): ")
#como asi que switch y case?
#es una forma diferente de escribir condicionales, donde se evalua un parametro , booleano y se a direccionar indirectamente segun de los casos definidos
match operador:
    case "+:":
        print("Resultado", num_1 + num_2)
    case "-" :
        print("Resultado", num_1 - num_2)
    case "*" :
        print("Resultado", num_1 * num_2)  
    case "/" :
        if num_2 != 0:
            print("Resultado", num_1 / num_2)
        else:
            print("Resultado no valido") 
    case _:
        print("Resultado no valido")           
 

