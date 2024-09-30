# cada um vai comer N pratos com brigadeiros
# os pratos são numerados de 1 a N
# cada prato possui 0 a 9 brigadeiros
# o grupo de amigos é formado por um subconjuntos dos alunos que possui K membros, incluindo a mim
# somando a quantidade que cada um do grupo irá comer
# o membro do grupo poder se mover para esquerda ou para direita
# somente uma troca pode ser realizada a cada segundo
# T segundos (trocas)
# tarefa: máximo número de brigadeiros o grupo pode comer
# primeira linha: N, K, T
# segunda linha: pratos de brigadeiros e N separados por espaços em branco. N = Pi. Pi a quantidade de brigadeiros no iEgésimo prato.
# terceira linha: posições iniciais dos alunos e contém N inteiros separados por espaço em branco. Gi indica se o aluno está sentado na iEgesima cadeira é membro ou não.
# Gi = 1 ou Gi = 0.

c = 0
soma = 0
num1 = 1
n1 = 0

l1 = input()
N, K, T = l1[0], l1[1], l1[2]
Nint = int(N)

l2 = input().split()
l3 = input().split()

for c in range(Nint):
    pos1 = c
    if l3[c] == '1' and pos1 != Nint:
        pos1 += 1
        intPos = int(l2[pos1])
        soma += intPos
    elif l3[c] == '1' and pos1 == Nint:
        pos1 = c
        if pos1 == 0:
            intPos = int(l2[pos1])
            soma += intPos
        else:
            pos1 -= 1

    c += 1

print(soma)
def calcular_brigadeiros(N, K, T, brigadeiros, posicoes):
    max_brigadeiros = 0
    for _ in range(T):
        for i in range(K):
            if posicoes[i] < N - 1 and brigadeiros[posicoes[i] + 1] > brigadeiros[posicoes[i]]:
                posicoes[i] += 1
        total_brigadeiros = sum(brigadeiros[pos] for pos in posicoes)
        max_brigadeiros = max(max_brigadeiros, total_brigadeiros)
    return max_brigadeiros

def ler_entrada():
    N, K, T = map(int, input().split())
    brigadeiros = list(map(int, input().split()))
    posicoes = list(map(int, input().split()))
    return N, K, T, brigadeiros, posicoes

def main():
    N, K, T, brigadeiros, posicoes = ler_entrada()
    if N < 1 or N > 50:
        return
    if K < 1 or K > 3:
        return
    if T < 1 or T > 1000:
        return
    if len(brigadeiros) != N:
        return
    if len(posicoes) != K:
        return
    resultados = calcular_brigadeiros(N, K, T, brigadeiros, posicoes)
    print(resultados)

if __name__ == "__main__":
    main()