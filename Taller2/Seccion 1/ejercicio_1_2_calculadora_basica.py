
while True:
    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        break
    except ValueError:
        print("Por favor ingresa números válidos.")

operacion = input("Ingresa la operación (+, -, *, /): ")

if operacion == "+":
    resultado = num1 + num2
    print(f"\nResultado: {num1} + {num2} = {resultado}")
elif operacion == "-":
    resultado = num1 - num2
    print(f"\nResultado: {num1} - {num2} = {resultado}")
elif operacion == "*":
    resultado = num1 * num2
    print(f"\nResultado: {num1} * {num2} = {resultado}")
elif operacion == "/":
    if num2 == 0:
        print("\nError: No se puede dividir entre cero.")
    else:
        resultado = num1 / num2
        print(f"\nResultado: {num1} / {num2} = {resultado}")
else:
    print("\nOperación no válida. Use +, -, * o /.")
