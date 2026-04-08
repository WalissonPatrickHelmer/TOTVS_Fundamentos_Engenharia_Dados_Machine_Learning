import pandas as pd

df = pd.read_csv(
    "data/processed/20230801_estacionamento_publico_motofrete_tratado.csv"
)

print(df.info())
print(df.head())