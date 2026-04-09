import pandas as pd

df = pd.read_csv(
    "data/gold/estacionamento_motofrete_analitico.csv"
)

print(df.head())
print(df.info())