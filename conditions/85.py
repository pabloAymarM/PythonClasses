#Crie um cronômetro

import time

totTime = int(input("Digite o número de segundos para o cronômetro: "))
print("Cronômetro iniciado...")

for i in range(totTime, -1, -1):
    min, sec = divmod(i, 60) 
    print(f"{min:02d}:{sec:02d}", end="\r")  
    time.sleep(1)

print("\nTempo finalizado!")