meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

temperaturas = []
somaTemp = 0

for numMes in range(12):
    temp = float(input(f"Digite a temperatura média de {meses[numMes]}: "))
    temperaturas.append(temp)

for cont in range(12):
    somaTemp += temperaturas[cont]

mediaAno = somaTemp / 12

print(f"\nA média anual de temperatura foi: {mediaAno:.2f}°C")

print("\nMeses com temperaturas acima da média anual:")
for numMes in range(12):
    if temperaturas[numMes] > mediaAno:
        print(f"{meses[numMes]} - {temperaturas[numMes]:.2f}°C")