# 🚀 Engenharia de Dados — Estacionamento Público Motofrete (Belo Horizonte)

Projeto completo de **Engenharia de Dados** utilizando dados públicos da Prefeitura de Belo Horizonte para análise de vagas destinadas ao **motofrete**.

> **Raw → Processed → Gold → Analytics → Visualização**

---

## 📊 Visão Geral

Este projeto realiza:

✅ Ingestão de múltiplos CSV mensais  
✅ Tratamento e padronização dos dados  
✅ Extração de coordenadas geográficas  
✅ Criação da camada analítica (GOLD)  
✅ Geração automática de gráficos  

---

## 🏗️ Arquitetura do Projeto


data/
├── raw/ → dados brutos
├── processed/ → dados tratados
└── gold/ → dados analíticos


Arquitetura baseada em:

- Bronze
- Silver
- Gold

---

## ⚙️ Tecnologias Utilizadas

- Python
- Pandas
- Matplotlib
- ETL Pipeline
- Data Analytics

---

## 🔄 Pipeline de Dados

### Extract — `extract.py`
Busca arquivos CSV mensais.

### Transform — `transform.py`
- Limpeza de encoding
- Padronização
- Conversão de tipos
- Extração de coordenadas

### Gold — `gold.py`

Gera métricas analíticas:

- Total de vagas físicas
- Total de vagas rotativas
- Registros por bairro

Output:


data/gold/estacionamento_motofrete_analitico.csv


---

## 📈 Visualizações

Execute:

```bash
python visualizacao.py
🥇 Ranking de vagas físicas

⚖️ Comparação vagas físicas vs rotativas

📦 Total de registros por bairro

🧭 Distribuição percentual

📊 Ranking horizontal

🧠 Insights
Região central concentra maior volume de vagas
Forte presença em áreas comerciais
Distribuição desigual entre bairros
Alta rotatividade logística
⭐ Pontos Fortes

✅ Pipeline completo de Engenharia de Dados
✅ Arquitetura Bronze → Silver → Gold
✅ Automação total
✅ Tratamento de dados reais
✅ Visualização automática

📂 Estrutura
.
├── data/
├── dashboard/
├── notebooks/
├── src/
├── visualizacao.py
├── requirements.txt
└── README.md
▶️ Como Executar
Criar ambiente
python -m venv .venv
Ativar (Windows)
.venv\Scripts\activate
Instalar dependências
pip install -r requirements.txt
Rodar pipeline
python src/transform.py
python src/gold.py
python visualizacao.py
👨‍💻 Autor

Walisson Patrick Helmer

📍 Belo Horizonte — MG

🔗 LinkedIn
https://www.linkedin.com/in/walissonpatrickhelmer/

💻 GitHub
https://github.com/WalissonPatrickHelmer

🚀 Próximos Passos
Dashboard interativo (Streamlit)
Banco de dados
Orquestração com Airflow
Deploy em Cloud

⭐ Se gostou do projeto, deixe uma estrela!


---

# ✅ AGORA FAÇA ISSO (PASSO FINAL)

Dentro do projeto:

```bash
git add .
git commit -m "fix: adiciona imagens no README"
git push
