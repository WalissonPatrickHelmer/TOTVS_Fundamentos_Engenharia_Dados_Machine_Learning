# src/transform.py

import pandas as pd
import glob
import os

print("🚀 transform.py iniciou")

# ===============================
# CONFIG
# ===============================

RAW_PATH = "data/raw/*.csv"
PROCESSED_PATH = "data/processed"

os.makedirs(PROCESSED_PATH, exist_ok=True)

# ===============================
# FUNÇÕES
# ===============================

def read_csv_safe(file_path):
    """
    Lê CSV tentando múltiplos encodings
    """
    print("📂 Lendo CSV com detecção de encoding...")

    for enc in ["utf-8", "utf-8-sig", "latin1"]:
        try:
            df = pd.read_csv(file_path, sep=";", encoding=enc)
            print(f"✅ Encoding usado: {enc}")
            return df
        except Exception:
            continue

    raise Exception("❌ Não foi possível ler o arquivo")


def clean_columns(df):
    """
    Limpa nomes das colunas
    """
    df.columns = (
        df.columns
        .str.replace("ï»¿", "", regex=False)
        .str.strip()
        .str.upper()
    )

    print("🧹 Colunas após limpeza:")
    print(df.columns.tolist())

    return df


def safe_numeric(df, column):
    """
    Converte coluna para número somente se existir
    """
    if column in df.columns:
        df[column] = pd.to_numeric(df[column], errors="coerce")
        print(f"✅ Convertido para numérico: {column}")
    else:
        print(f"⚠️ Coluna não encontrada: {column}")

    return df


def extract_coordinates(df):
    """
    Extrai latitude e longitude se existir coluna LOGRADOURO ou coordenadas
    (ajuste conforme seu dataset)
    """

    print("📍 Extraindo coordenadas...")

    # exemplo genérico — adapta depois se quiser
    if "LATITUDE" in df.columns and "LONGITUDE" in df.columns:
        df["LATITUDE"] = pd.to_numeric(df["LATITUDE"], errors="coerce")
        df["LONGITUDE"] = pd.to_numeric(df["LONGITUDE"], errors="coerce")

    else:
        print("⚠️ Coordenadas não encontradas no arquivo")

    return df


# ===============================
# PIPELINE
# ===============================

print("📂 Buscando arquivos CSV...")

files = glob.glob(RAW_PATH)

for file in files:

    print(f"\n📄 Processando: {file}")

    # ---------- leitura ----------
    df = read_csv_safe(file)

    # ---------- limpeza ----------
    print("🧹 Limpando dados...")
    df = clean_columns(df)

    # ---------- conversões seguras ----------
    df = safe_numeric(df, "NUMERO_VAGAS_FISICAS")
    df = safe_numeric(df, "NUMERO_VAGAS_ROTATIVAS")
    df = safe_numeric(df, "TEMPO_PERMANENCIA")

    # ---------- coordenadas ----------
    df = extract_coordinates(df)

    # ---------- salvar ----------
    filename = os.path.basename(file)
    output_name = filename.replace(".csv", "_tratado.csv")

    output_path = os.path.join(PROCESSED_PATH, output_name)

    df.to_csv(output_path, index=False, encoding="utf-8-sig")

    print(f"✅ Arquivo salvo em: {output_path}")

print("\n🎯 Pipeline finalizado com sucesso!")

