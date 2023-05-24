def converter_fahrenheit_para_celsius(fahrenheit):
    celsius = 5 * ((fahrenheit - 32) / 9)
    return celsius

fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))
celsius = converter_fahrenheit_para_celsius(fahrenheit)

print(f"A temperatura em graus Celsius é: {celsius:.2f}°C")
