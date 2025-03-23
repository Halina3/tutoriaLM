for a in range(-100, 101, 2):  
    for b in range(-100, 101, 2):  
        soma = a + b
        if soma % 2 == 1:  
            print(f"Erro: {a} + {b} = {soma}, que é ímpar!")
            break
    else:
        continue
    break
else:
    print("Comprovado: A soma de dois números pares sempre resulta em um número par.")
