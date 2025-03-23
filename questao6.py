def divide(x, y):
    return y % x == 0  

for a in range(1, 10):
    for b in range(a, 50, a):  
        for c in range(b, 100, b):  
            if not divide(a, c):
                print(f"Erro: {a} não divide {c}")
                break
        else:
            continue
        break
    else:
        continue
    break
else:
    print("Comprovado: Se a|b e b|c, então a|c.")
