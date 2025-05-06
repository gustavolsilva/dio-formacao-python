# Estrutura de Dados

## Listas
## Objetivo Geral
<p>Entender o funcionamento da estrutura de dados lista. </p>

## Criando listas

<p> Listas em Python podem armazenar de maneira sequencial qualquer tipo de objeto. Podemos criar listas utilizando o construtor <b>list</b>, a função range ou colocando valores separados por vírgula dentro de colchetes. Listas são objetos mutáveis, portanto podemos alterar seus valores após a criação</p>

### Exemplo

```
frutas = ["laranja", "maca", "uva"]

frutas = []

letras = list("python")

numeros = list(range(10))

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]

```

## Acesso direto

<p> A lista é uma sequência. Portanto, podemos acessar seus dados utilizando índices. Cotamos o índice de determinada sequencia a partir do zero.</p>

### Exemplo

```
frutas = ["maca", "laranja", "uva", "pera"]

frutas[0] # "maca"

frutas[2] # "uva"
```

## Indices negativos

<p> Sequencias suportam indexação negativa. A contagem começa em -1.

### Exemplo

```
frutas = ["maca", "laranja", "uva", "pera"]
frutas[-1] # "pera"
frutas[-3] # "laranja"
```

## Listas aninhadas

<p> Listas podem armazenar todos os tipos de objetos Python. Portanto, podemos ter listas que armazenam outras listas. Com isso, podemos criar estruturas bidimensionais (tabelas), e acessar informando os índices de linha e coluna.</p>

### Exemplo

```
matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

matriz[0] # [1, "a", 2]
matriz[0][0] # 1
matriz[0][-1] # 2
matriz[-1][-1] # "c"
```
## Fatiamento
<p> Além de acessar os elementos diretamente, podemos extrair um conjunto de valores de uma sequencia. Para isso, basta passar o índice inicial e/ou final para acessar o conjunto. Podemos ainda informar quantas posiç~eos o cursos deve "pular" no acesso.</p>

### Exemplo

```
lista = ["p", "y", "t", "h", "o", "n"]

lista[2:] # ["t", "h", "o", "n"]
lista[:2] # ["p", "y"]
lista[1:3]  # ["y", "t"]
lista[0:3:2] # ["p", "t"]
lista[::] # ["p", "y", "t", "h", "o", "n"]
lista[::-1] # ["n", "o", "h", "t", "y", "p"]
```
## Iterar listas
<p> A forma mais comum para percorrer os dados de uma lista é utilizando o comando <b>for</b>.</p>

### Exemplo

```
carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)
```

## Função enumerate
<p> As vezes é necessário saber qual índice do objeto dentro do laço <b>for</b>. Para isso, podemos utilizar a função <b>enumerate</b>. </p>

### Exemplo

```
carros = ["gol", "celta", "palio"]

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
```

## Compreensão de listas

<p> A compreensão de lista (list comprehension) oferece uma sintaxe mais curta quando você deseja: criar uma nova lista com base nos valores de uma lista existente (filtro) ou gerar uma nova lista aplicando alguma modificação nos elementos de uma lista existente.</p>

### Filtro versão 1

```
numeros = [1, 30, 21, 2, 9, 65, 34]
numeros_pares = []

for numero in numeros:
    if numero % 2 == 0:
        numeros_pares.append(numero)
```

### Filtro versão 2

```
numeros = [1, 30, 21, 2, 9, 65, 34]

# variavel = [retorno for variavel in lista if condicao]
numeros_pares = [numero for numero in numeros if numero % 2 == 0]

```

### Modificando valores versão 1

```
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)
```

### Modificando valores versão 2

```
numeros = [1, 30, 21, 2, 9, 65, 34]
# variavel = [retorno for variavel in lista]
quadrado = [numero ** 2 for numero in numeros]
```

## Metodos da classe list

### [].append

```
lista = []
lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print (lista) # [1, "Python", [40, 30, 20]]
```

### [].clear

```
lista = [1, "Python", [40, 30, 20]]

print(lista) # [1, "Python", [40, 30, 20]]

lista.clear()

print(lista) # []
```

### [].copy

```
lista = [1, "Python", [40, 30, 20]]

lista.copy()

print(lista) # [1, "Python", [40, 30, 20]]

```

### [].count

```
cores = ["vermelho", "azul", "verde", "azul"]

cores.count("vermelho") # 1
cores.count("azul") # 2
cores.count("verde") # 1

```