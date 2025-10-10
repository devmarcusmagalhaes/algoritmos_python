def converterCelsius(grau):
    grauCelsius = grau
    grauFahrenheit = grauCelsius * 1.8 + 32
    return grauFahrenheit


def converterFahrenheit(grau):
    grauFahrenheit = grau
    grauCelsius = (grauFahrenheit - 32) / 1.8
    return grauCelsius


def escolherConversao(opcao):
    grau = float(input("Digite o grau a ser convertido: "))

    match opcao:
        case 1:
            resultado = converterCelsius(grau)
            print(f"Resultado: {resultado:.2f} °F")
        case 2:
            resultado = converterFahrenheit(grau)
            print(f"Resultado: {resultado:.2f} °C")
        case _:
            print("Opção inválida")


print("--- Escolha uma opção ---")
opcao = int(input(
    "1 - Converter Celsius para Fahrenheit\n2 - Converter Fahrenheit para Celsius\nDigite: "))

escolherConversao(opcao)
