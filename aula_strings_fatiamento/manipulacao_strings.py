#%%
curso = "pYthon"

# %%
# Caracteres em Maiusculo
print(curso.upper())

# Caracteres em Minusculo
print(curso.lower())

# Capitaliza a primeira letra
print(curso.title())

# %%
curso = "       Python"

# %%
# Remove os espaços em branco do inicio e do fim
print(curso.strip())

# Remove os espaços em branco do inicio
print(curso.lstrip())

# Remove os espaços em branco do fim
print(curso.rstrip())
# %%

curso = "Python"
# %%

# preenche a string com o caracter # e centraliza
print(curso.center(10, "#")) # P

# %%

# Junção entre o caracter . com os caracteres da string
print(".".join(curso)) # P.y.t.h.o.n
# %%