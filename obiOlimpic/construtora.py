def calcular_fases(N, alturas):
    fases = 0
    while True:
        max_altura = max(alturas)
        min_altura = min(alturas)
        if max_altura == min_altura:
            break
        fases += 1
        for i in range(N):
            if alturas[i] < max_altura:
                alturas[i] += 1
    return fases

def ler_entrada():
    N = int(input())
    alturas = list(map(int, input().split()))
    return N, alturas

def main():
    N, alturas = ler_entrada()
    if N < 1:
        print("Erro: N deve ser maior ou igual a 1.")
        return
    if len(alturas) != N:
        print("Erro: O número de alturas deve ser igual a N.")
        return
    fases = calcular_fases(N, alturas)
    print(fases)

if __name__ == "__main__":
    main()