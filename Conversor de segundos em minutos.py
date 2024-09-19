def converter_tempo(valor, unidade_origem, unidade_destino):
    # Converte o valor para segundos
    if unidade_origem == 'segundos':
        segundos = valor
    elif unidade_origem == 'minutos':
        segundos = valor * 60
    elif unidade_origem == 'horas':
        segundos = valor * 3600

    # Converte de segundos para a unidade de destino
    if unidade_destino == 'segundos':
        return segundos
    elif unidade_destino == 'minutos':
        return segundos / 60
    elif unidade_destino == 'horas':
        return segundos / 3600


def main():
    print("Escolha a unidade de origem (segundos, minutos, horas):")
    unidade_origem = input().strip().lower()

    print("Escolha a unidade de destino (segundos, minutos, horas):")
    unidade_destino = input().strip().lower()

    print(f"Digite a quantidade de {unidade_origem} que deseja converter:")
    valor = float(input())

    resultado = converter_tempo(valor, unidade_origem, unidade_destino)
    print(f"{valor} {unidade_origem} é igual a {resultado} {unidade_destino}")


if __name__ == "__main__":
    main()
