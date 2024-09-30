def calcular_intersecoes(N, X1, X2, linhas):
    intersecoes = 0
    for i in range(N):
        for j in range(i + 1, N):
            A1, B1 = linhas[i]
            A2, B2 = linhas[j]
            if A1 != A2:
                x = (B2 - B1) / (A1 - A2)
                if X1 <= x <= X2:
                    intersecoes += 1
            elif A1 == A2 and B1 != B2:
                continue
            elif A1 == A2 and B1 == B2:
                intersecoes += 1
    return intersecoes

N, X1, X2 = map(int, input().split())
linhas = []
for _ in range(N):
    A, B = map(int, input().split())
    linhas.append((A, B))

print(calcular_intersecoes(N, X1, X2, linhas))