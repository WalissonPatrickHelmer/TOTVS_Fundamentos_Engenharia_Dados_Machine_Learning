# 🚀 Engenharia de Dados — Estacionamento Público Motofrete (Belo Horizonte)

Projeto completo de **Engenharia de Dados** utilizando dados públicos da Prefeitura de Belo Horizonte para análise de vagas destinadas ao **motofrete**.

O objetivo foi construir um pipeline real seguindo arquitetura moderna de dados:

> **Raw → Processed → Gold → Analytics → Visualização**

---

## 📊 Visão Geral

Este projeto realiza:

✅ Ingestão de múltiplos arquivos CSV mensais  
✅ Tratamento e padronização dos dados  
✅ Extração de coordenadas geográficas  
✅ Criação de camada analítica (GOLD)  
✅ Geração automática de gráficos  
✅ Estrutura profissional de Data Pipeline

---

## 🏗️ Arquitetura do Projeto


data/
│
├── raw/ → dados brutos
├── processed/ → dados tratados (Silver)
└── gold/ → dados analíticos finais


Pipeline inspirado em arquiteturas modernas:

- Bronze (Raw)
- Silver (Transformação)
- Gold (Analytics)

---

## ⚙️ Tecnologias Utilizadas

- Python
- Pandas
- Matplotlib
- ETL Pipeline
- Data Modeling
- Análise Exploratória de Dados

---

## 🔄 Pipeline de Dados

### 1️⃣ Extract (`extract.py`)
- Busca arquivos CSV mensais
- Centraliza ingestão de dados

### 2️⃣ Transform (`transform.py`)
- Limpeza de encoding (UTF-8 / BOM)
- Padronização de colunas
- Conversão de tipos
- Extração de coordenadas do campo `GEOMETRIA`
- Geração da camada **Processed**

### 3️⃣ Gold Layer (`gold.py`)
Criação das métricas analíticas:

- Total de vagas físicas
- Total de vagas rotativas
- Quantidade de registros por bairro

Resultado:


data/gold/estacionamento_motofrete_analitico.csv


---

## 📈 Visualizações Automáticas

Os gráficos são gerados automaticamente com:

```bash
python visualizacao.py
📊 Resultados
🥇 Ranking de vagas físicas

⚖️ Comparação vagas físicas vs rotativas

📦 Total de registros por bairro

🧭 Distribuição percentual

📊 Ranking horizontal (visual executivo)

🧠 Insights Obtidos
Região central concentra maior volume de vagas de motofrete
Forte presença em áreas comerciais estratégicas
Distribuição desigual entre bairros
Alta rotatividade em regiões de logística urbana
⭐ Pontos Fortes do Projeto

✅ Pipeline completo de Engenharia de Dados
✅ Separação em camadas (Raw / Processed / Gold)
✅ Automação total do fluxo
✅ Tratamento de inconsistências reais de dados públicos
✅ Conversão e padronização de encoding CSV
✅ Estrutura semelhante a projetos corporativos
✅ Geração automática de analytics

📂 Estrutura do Repositório
.
├── data
│   ├── raw
│   ├── processed
│   └── gold
│
├── src
│   ├── extract.py
│   ├── transform.py
│   └── gold.py
│
├── notebooks
│   └── análises exploratórias
│
├── dashboard
│   └── gráficos gerados automaticamente
│
├── visualizacao.py
├── requirements.txt
└── README.md
▶️ Como Executar
1️⃣ Criar ambiente virtual
python -m venv .venv
2️⃣ Ativar

Windows:

.venv\Scripts\activate
3️⃣ Instalar dependências
pip install -r requirements.txt
4️⃣ Executar pipeline
python src/transform.py
python src/gold.py
python visualizacao.py
🎯 Objetivo Profissional

Este projeto demonstra habilidades em:

Engenharia de Dados
ETL
Modelagem Analítica
Automação em Python
Storytelling com Dados
👨‍💻 Autor

Walisson Patrick Helmer

📍 Belo Horizonte — MG
🔗 LinkedIn: https://www.linkedin.com/in/walissonpatrickhelmer/

💻 GitHub: https://github.com/WalissonPatrickHelmer

🚀 Próximos Passos (Roadmap)
Dashboard interativo (Streamlit)
Integração com banco de dados
Orquestração com Airflow
API de consulta dos dados
Deploy em Cloud

⭐ Se este projeto foi útil, deixe uma estrela no repositório!


---

# 🔥 Resultado

Quando subir no GitHub:

✅ imagens aparecem automaticamente  
✅ README vira página visual  
✅ parece projeto de engenheiro de dados pleno  

---

Se quiser, no próximo passo eu te mostro algo que muda MUITO o impacto:

👉 **como transformar esse projeto em um post viral no LinkedIn (estrutura pronta + storytelling)** — praticamente garantia de engajamento.

Só dizer: **"vamos montar o post"** 🚀.