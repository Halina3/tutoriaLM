for a in range(-99, 100, 2):  
    for b in range(-99, 100, 2):  
        produto = a * b
        if produto % 2 == 0:  
            print(f"Erro: {a} * {b} = {produto}, que é par!")
            break
    else:
        continue
    break
else:
    print("Comprovado: O produto de dois números ímpares sempre resulta em um número ímpar.")
