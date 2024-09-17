#Escreva um program que leia um valor em metros e o exiba convetendo para centímetros e milímetros:
m = float(input('Digite a medida em metro: '))
km = m / 1000
hm = m / 100
dam = m / 10
m = m
dm = m * 10
cm = m * 100
mm = m * 1000

print ('km: {}; \nhm: {}; \ndam: {}; \nm: {:.0f}; \ndm: {:.0f}; \ncm: {:.0f}; \nmm: {:.0f}.' .format(km, hm, dam, m, dm, cm, mm))
 