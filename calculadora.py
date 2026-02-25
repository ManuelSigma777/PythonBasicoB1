# Mi calculadora

print("✪✪ CALCULADORA ✪✪")
num1 = float(input("Escribe el primer numero: "))
num2 = float(input("Escribe el segundo numero: "))
op = input("¿Cual operacion deseas hacer? (+)(-)(*)(/)")

def suma(num_1, num_2):
    return num_1 + num_2

def resta(num_1, num_2):
    return num_1 - num_2

def mult(num_1, num_2):
    return num_1 * num_2

def div(num_1, num_2):
    return num_1 / num_2


if op == "+":
    resultado = suma(num1, num2)
    print("El resultado de la suma es: ", resultado)

if op == "-":
    resultado = resta(num1, num2)
    print("El resultado de la resta es: ", resultado)

if op == "*":
    resultado = mult(num1, num2)
    print("El resultado de la multiplicacion es: ", resultado)

if op == "/":
    resultado = div(num1, num2)
    print("El resultado de la division es: ", resultado)