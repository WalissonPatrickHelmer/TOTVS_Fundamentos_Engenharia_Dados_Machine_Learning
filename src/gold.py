import pandas as pd
import glob
import os

print("🥇 Iniciando camada GOLD...")

# ===============================
# Buscar arquivos tratados
# ===============================
arquivos = glob.glob("data/processed/*_tratado.csv")

lista_df = []

for arquivo in arquivos:
    print(f"📄 Lendo: {arquivo}")
    df = pd.read_csv(arquivo)
    lista_df.append(df)

# ===============================
# Unir todos os meses
# ===============================
df_total = pd.concat(lista_df, ignore_index=True)

print("✅ Arquivos unidos!")

# ===============================
# Agregações analíticas
# ===============================
print("📊 Criando métricas...")

gold = (
    df_total
    .groupby(["BAIRRO", "TIPO_ESTACIONAMENTO"])
    .agg(
        TOTAL_VAGAS_FISICAS=("NUMERO_VAGAS_FISICAS", "sum"),
        TOTAL_VAGAS_ROTATIVAS=("NUMERO_VAGAS_ROTATIVAS", "sum"),
        TOTAL_REGISTROS=("ID_EDESP", "count")
    )
    .reset_index()
)

# ===============================
# ✅ CORREÇÃO PROFISSIONAL (AQUI)
# transformar floats em inteiros
# ===============================
gold["TOTAL_VAGAS_FISICAS"] = gold["TOTAL_VAGAS_FISICAS"].astype(int)
gold["TOTAL_VAGAS_ROTATIVAS"] = gold["TOTAL_VAGAS_ROTATIVAS"].astype(int)

# ===============================
# Ordenar
# ===============================
gold = gold.sort_values(
    by="TOTAL_VAGAS_FISICAS",
    ascending=False
)

# ===============================
# Salvar dataset GOLD
# ===============================
os.makedirs("data/gold", exist_ok=True)

output = "data/gold/estacionamento_motofrete_analitico.csv"

gold.to_csv(output, index=False)

print("✅ Dataset GOLD criado!")
print(f"📁 Salvo em: {output}")