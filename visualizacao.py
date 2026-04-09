import pandas as pd
import matplotlib.pyplot as plt
import os

print("📊 Gerando gráficos...")

# ===============================
# Criar pasta dashboard
# ===============================
os.makedirs("dashboard", exist_ok=True)

# ===============================
# Ler dataset GOLD
# ===============================
df = pd.read_csv(
    "data/gold/estacionamento_motofrete_analitico.csv"
)

# ===============================
# TOP 10 bairros
# ===============================
top10 = df.sort_values(
    by="TOTAL_VAGAS_FISICAS",
    ascending=False
).head(10)

# ===============================
# 1️⃣ Ranking vagas físicas
# ===============================
plt.figure()

plt.bar(top10["BAIRRO"], top10["TOTAL_VAGAS_FISICAS"])
plt.xticks(rotation=45)
plt.title("Top 10 Bairros - Vagas Físicas")

plt.tight_layout()
plt.savefig("dashboard/01_ranking_vagas_fisicas.png")
plt.close()

# ===============================
# 2️⃣ Físicas vs Rotativas
# ===============================
plt.figure()

x = range(len(top10))

plt.bar(x, top10["TOTAL_VAGAS_FISICAS"], label="Físicas")
plt.bar(x, top10["TOTAL_VAGAS_ROTATIVAS"], bottom=top10["TOTAL_VAGAS_FISICAS"], label="Rotativas")

plt.xticks(x, top10["BAIRRO"], rotation=45)
plt.title("Vagas Físicas vs Rotativas")
plt.legend()

plt.tight_layout()
plt.savefig("dashboard/02_comparacao_vagas.png")
plt.close()

# ===============================
# 3️⃣ Total registros
# ===============================
plt.figure()

plt.bar(top10["BAIRRO"], top10["TOTAL_REGISTROS"])
plt.xticks(rotation=45)
plt.title("Top 10 - Registros de Motofrete")

plt.tight_layout()
plt.savefig("dashboard/03_total_registros.png")
plt.close()

# ===============================
# 4️⃣ Participação percentual
# ===============================
plt.figure()

plt.pie(
    top10["TOTAL_VAGAS_FISICAS"],
    labels=top10["BAIRRO"],
    autopct="%1.1f%%"
)

plt.title("Distribuição de Vagas por Bairro")

plt.savefig("dashboard/04_distribuicao_percentual.png")
plt.close()

# ===============================
# 5️⃣ Gráfico horizontal (LinkedIn)
# ===============================
plt.figure()

plt.barh(top10["BAIRRO"], top10["TOTAL_VAGAS_FISICAS"])
plt.title("Ranking Horizontal - Vagas de Motofrete")

plt.tight_layout()
plt.savefig("dashboard/05_ranking_horizontal.png")
plt.close()

print("✅ 5 gráficos criados na pasta /dashboard")