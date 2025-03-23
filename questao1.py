for n in range(-100, 101):
    quadrado = n ** 2
    if quadrado % 2 == 1:
        if n % 2 == 0:
            print(f"Erro: {n} é par, mas {quadrado} é ímpar!")
            break
else:
    print("Comprovado: sempre que o quadrado é ímpar, o número original também é ímpar.")
