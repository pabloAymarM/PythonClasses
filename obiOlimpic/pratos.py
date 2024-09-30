def calcular_fases(N, M, K, alturas, feiticos, refeicoes):
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
        for j in range(M):
            if refeicoes[j][0] > 1:
                alturas = [alturas[k] * refeicoes[j][0] + refeicoes[j][1] for k in range(N)]
        for k in range(K):
            if feiticos[k][0] > 1:
                alturas = [alturas[l] * feiticos[k][0] + feiticos[k][1] for l in range(N)]
    return fases

def ler_entrada():
    N, M, K = map(int, input().split())
    alturas = list(map(int, input().split()))
    feiticos = []
    for _ in range(K):
        feitico = list(map(int, input().split()))
        feiticos.append(feitico)
    refeicoes = []
    for _ in range(M):
        refeicao = list(map(int, input().split()))
        refeicoes.append(refeicao)
    return N, M, K, alturas, feiticos, refeicoes

def main():
    N, M, K, alturas, feiticos, refeicoes = ler_entrada()
    if N < 1:
        print("Erro: N deve ser maior ou igual a 1.")
        return
    if M < 1:
        print("Erro: M deve ser maior ou igual a 1.")
        return
    if K < 1:
        print("Erro: K deve ser maior ou igual a 1.")
        return
    if len(alturas) != N:
        print("Erro: O número de alturas deve ser igual a N.")
        return
    if len(feiticos) != K:
        print("Erro: O número de feitiços deve ser igual a K.")
        return
    if len(refeicoes) != M:
        print("Erro: O número de refeições deve ser igual a M.")
        return
    fases = calcular_fases(N, M, K, alturas, feiticos, refeicoes)
    print(fases)

if __name__ == "__main__":
    main()