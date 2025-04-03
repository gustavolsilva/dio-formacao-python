# %%
## Old stile %
nome = "Gustavo"
idade = 39
profissao = "Engenheiro de Dados"
linguagem = "Python"

print("Ola, me chamo %s. Eu tenho %d anos, trabalho como %s. Estou matriculado no curso de %s." % (nome, idade, profissao, linguagem))
# %%

## Metodo format()
nome = "Gustavo"
idade = 39
profissao = "Engenheiro de Dados"
linguagem = "Python"

pessoa: dict = {
    "nome": nome,
    "idade": idade,
    "profissao": profissao,
    "linguagem": linguagem
}

print("Ola, me chamo {}. Eu tenho {} anos, trabalho como {}. Estou matriculado no curso de {}.".format(nome, idade, profissao, linguagem))

print("Ola, me chamo {3}. Eu tenho {2} anos, trabalho como {1}. Estou matriculado no curso de {0}.".format(linguagem, profissao, idade, nome))

print("Olá, me chamo {nome}. Eu tenho {idade} anos, trabalho como {profissao}. Estou matriculado no curso de {linguagem}.".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))

print("Olá, me chamo {nome}. Eu tenho {idade} anos, trabalho como {profissao}. Estou matriculado no curso de {linguagem}.".format(**pessoa))

# %%

nome = "Gustavo"
idade = 39
profissao = "Engenheiro de Dados"
linguagem = "Python"

print(f"Olá, me chamo {nome}. Eu tenho {idade} anos, trabalho como {profissao}. Estou matriculado no curso de {linguagem}.")

# %%

## F-strings
PI = 3.14159

print(f"Valor de PI: {PI:.2f}")
print(f"Valor de PI: {PI:10.2f}")