import pandas as pd

gold = pd.read_csv("data/gold/estacionamento_motofrete_analitico.csv")

print(gold.sort_values("BAIRRO"))

