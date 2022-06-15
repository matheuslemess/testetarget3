import json
from webbrowser import get
from distro import info
from numpy import intp
from pyrsistent import m

with open("dados.json") as teste3:
    dados = json.load(teste3)

    dados = []
    maior = 0
    menor = 0
    media = 0

for c in range(0, 5):
    dados.append(int(input(f'Digite um valor para a posição {c}')))
    if c == 0:
        maior = menor = dados[c]
    else:
        if dados[c] > maior:
            maior = dados[c]
        if dados[c] < maior:
            menor = dados[c]
        if dados[c] > media:
            media = dados[c]

print('=-'*30)
print(f'Você digitou os valores {dados}')
print(f'O maior numero da lista foi {maior} nas posições')
for i, v in enumerate(dados):
    if v == maior:
        print(f'{i}...', end='')

print()
print(f'O maior numero da lista foi {menor} nas posições', end='')
for i, v in enumerate(dados):
    if v == menor:
        print(f'{i}...', end='')

print('=-'*30)
print(f'Você digitou os valores {dados}')
print(f'O maior numero da lista foi {media} nas posições')
for i, v in enumerate(dados):
    if v == media:
        print(f'{i}...', end='')
