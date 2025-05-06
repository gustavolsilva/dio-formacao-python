# %%
carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)

# %%
# Funcao Enumerate
carros = ["gol", "celta", "palio"]

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")