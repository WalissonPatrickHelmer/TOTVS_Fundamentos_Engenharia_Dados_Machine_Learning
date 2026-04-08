import pandas as pd
from pathlib import Path


def extract_data():
    """
    Etapa Extract do ETL:
    Lê dados brutos de um arquivo CSV.
    """

    caminho_arquivo = Path("data/raw/usuarios.csv")

    if not caminho_arquivo.exists():
        print("Arquivo não encontrado!")
        return None

    df = pd.read_csv(caminho_arquivo)

    print("Dados extraídos com sucesso!")
    print(df.head())

    return df


if __name__ == "__main__":
    extract_data()