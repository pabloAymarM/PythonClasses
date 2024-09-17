#! /usr/bin/env python3

"""
 * OBI 2023 - Fase 3
 * Balanceamento de Pirâmide - Solução com ordenação e força bruta
 * Mateus Bezrutchka
"""

x = [int(x) for x in input().split()]
soma = sum(x)

if soma % 3 != 0:
  # se a soma nao é divisivel por 3, é impossivel
  print("N")
  quit()

# o maior valor deve estar no terceiro andar
x.sort()
if x[5] != soma / 3:
  print("N")
  quit()

# temos que achar outros dois pro segundo andar
for i in range(5):
  for k in range(i + 1, 5):
    if x[i] + x[k] == soma / 3:
      print("S")
      quit()

# se chegamos aqui, nao achamos par pro segundo andar
print("N")
