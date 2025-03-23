for a in range(-100, 101, 2):  
    for b in range(-100, 101, 2):  
        produto = a * b
        if produto % 2 == 1:  
            print(f"Erro: {a} * {b} = {produto}, que é ímpar!")
            break
    else:
        continue
    break
else:
    print("Comprovado: O produto de dois números pares sempre resulta em um número par.")
