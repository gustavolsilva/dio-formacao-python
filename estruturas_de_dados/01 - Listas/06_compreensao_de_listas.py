
# %%
# Filtro na versão 1
numeros = [1, 30, 21, 2, 9, 65, 34]
numeros_pares = []

for numero in numeros:
    if numero % 2 == 0:
        numeros_pares.append(numero)

print(numeros)
print(numeros_pares)
# %%
# Filtro na versão 2
numeros = [1, 30, 21, 2, 9, 65, 34]
# variavel = [retorno for variavel in lista if condicao]
numeros_pares = [numero for numero in numeros if numero % 2 == 0]
print(numeros)
print(numeros_pares)
# %%
### Modificando valores versão 1
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)

print(numeros)
print(quadrado)
# %%
# Modificando valores versão 2
numeros = [1, 30, 21, 2, 9, 65, 34]
# variavel = [retorno for variavel in lista]
quadrado = [numero ** 2 for numero in numeros]
print(numeros)
print(quadrado)
