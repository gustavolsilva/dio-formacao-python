# %%
nome = "gusTavO"

# %%
print(nome.upper())  # Converte a string para maiúsculas
print(nome.lower())  # Converte a string para minúsculas
print(nome.title())  # Converte a string para título (primeira letra maiúscula) 
# %%

texto = "  Olá mundo!    "

# %%
print(texto+".")
print(texto.strip()+".")  # Remove espaços em branco no início e no final da string 
print(texto.lstrip()+".")  # Remove espaços em branco no início da string
print(texto.rstrip()+".")  # Remove espaços em branco no final da string

# %%
menu = "Python"
# %%
print("####"+ menu+"####")
# %%
print(menu.ljust(14))  # Alinha à esquerda a string em um total de 14 caracteres
print(menu.center(14, "#"))  # Centraliza a string em um total de 14 caracteres, preenchendo com "#"
# %%
print("P-y-t-h-o-n")
print("-".join(menu))  # Junta os caracteres da string com "-" entre eles
