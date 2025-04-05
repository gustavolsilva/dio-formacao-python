#%%

nome = "Gustavo"
idade = 39
profissao = "Engenheiro de Dados"
linguagem = "Python"
# %%
# Old style
print("Nome: %s Idade: %d" % (nome, idade))
# %%
print("Nome: {} Idade: {}" .format(nome, idade))
print("Nome: {1} Idade: {0}" .format(idade, nome))
print("Nome: {1} Idade: {0} Nome: {1} {1}" .format(idade, nome))
print("Nome: {nome} Idade: {idade}" .format(nome=nome, idade=idade))
print("Nome: {name} Idade: {age}" .format(age=idade, name=nome ))

# %%
saldo = 45.435
dados = {
    "nome": nome,
    "idade": idade,

}

print("Nome: {nome} Idade: {idade}" .format(**dados))
# %%

# f-string
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.1f}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.2f}")

# %%
