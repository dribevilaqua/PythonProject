primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
decimo = primeiro + (10-1) * razão
#formula do n ésimo número
for c in range(primeiro,decimo + razão,razão):
    print('{}'.format(c), end=' - ')
print('Acabou')

# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.