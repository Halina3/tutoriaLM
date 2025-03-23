for par in range(-100, 101, 2):   
    for impar in range(-99, 102, 2):  
        soma = par + impar
        if soma % 2 == 0:  
            print(f"Erro: {par} + {impar} = {soma}, que é par!")
            break
    else:
        continue
    break
else:
    print("Comprovado: A soma de um número par com um número ímpar sempre resulta em um número ímpar.")
