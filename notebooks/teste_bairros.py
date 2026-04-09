import pandas as pd
import glob

print("🔎 Verificando bairros existentes...")

arquivos = glob.glob("data/processed/*_tratado.csv")

lista = []

for arq in arquivos:
    df = pd.read_csv(arq)
    lista.append(df)

df_total = pd.concat(lista, ignore_index=True)

# listar bairros únicos
bairros = sorted(df_total["BAIRRO"].dropna().unique())

print(f"\n✅ Total de bairros encontrados: {len(bairros)}\n")

for b in bairros:
    print(b)