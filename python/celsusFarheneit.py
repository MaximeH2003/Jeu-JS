def convertir_celsius_vers_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

def convertir_fahrenheit_vers_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Conversion de Celsius vers Fahrenheit
temp_celsius = float(input("Entrez la température en Celsius : "))
temp_fahrenheit = convertir_celsius_vers_fahrenheit(temp_celsius)
print("La température en Fahrenheit est :", temp_fahrenheit)

# Conversion de Fahrenheit vers Celsius
temp_fahrenheit = float(input("Entrez la température en Fahrenheit : "))
temp_celsius = convertir_fahrenheit_vers_celsius(temp_fahrenheit)
print("La température en Celsius est :", temp_celsius)