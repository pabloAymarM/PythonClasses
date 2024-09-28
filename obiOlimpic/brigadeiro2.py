# Leitura da primeira linha de entrada
N, K, T = map(int, input().split())

# Leitura dos brigadeiros em cada prato
l2 = list(map(int, input().split()))

# Leitura das posições iniciais dos amigos (1 se é amigo, 0 se não é)
l3 = list(map(int, input().split()))

# Soma máxima de brigadeiros
soma = 0

# Simulação das trocas
for t in range(min(T, N - 1)):  # Realizar no máximo N-1 trocas
    houveTroca = False
    for i in range(N):
        if l3[i] == 1:  # Verificar se é um amigo
            # Tentativa de mover o amigo para a direita
            if i < N - 1 and l3[i + 1] == 0 and l2[i + 1] > l2[i]:
                # Realiza a troca
                l3[i], l3[i + 1] = l3[i + 1], l3[i]
                houveTroca = True
            # Tentativa de mover o amigo para a esquerda
            elif i > 0 and l3[i - 1] == 0 and l2[i - 1] > l2[i]:
                # Realiza a troca
                l3[i], l3[i - 1] = l3[i - 1], l3[i]
                houveTroca = True
    if not houveTroca:
        break  # Se não houve trocas, paramos a simulação

# Cálculo da soma dos brigadeiros nas posições finais dos amigos
for i in range(N):
    if l3[i] == 1:
        soma += l2[i]

# Exibir o resultado
print(soma)
