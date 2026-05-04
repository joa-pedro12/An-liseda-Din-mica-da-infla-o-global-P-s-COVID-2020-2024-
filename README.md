# Anlise da Dinmica da inflação global Pós-COVID-2020-2024

# 📊 Projeto de Análise de Dados — Brasil vs Mundo

## 🎯 Objetivo

Este projeto tem como objetivo analisar o comportamento da inflação no Brasil em comparação com a média global no período pós-COVID.

---

## 📁 Estrutura do Projeto

```bash
project/
│
├── data/
│   ├── raw/          # dados brutos (não modificados)
│   ├── processed/    # dados limpos
│   └── curated/      # dados prontos para análise
│
├── notebooks/        # exploração de dados
│
├── src/
│   ├── ingestion/    # coleta e leitura de dados
│   ├── processing/   # limpeza e transformação
│   └── analysis/     # análise e visualização
│
├── outputs/          # gráficos e resultados
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🔄 Pipeline de Dados

Fluxo utilizado no projeto:

RAW → PROCESSADO → CURADO → ANÁLISE

---

## 🧠 Tecnologias Utilizadas

* Python
* Pandas
* Plotly
* Streamlit

---

## 🚀 Como rodar o projeto

1. Clone o repositório:

```bash
git clone URL_DO_REPOSITORIO
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Execute a aplicação (quando disponível):

```bash
streamlit run src/analysis/app.py
```

---

## 👥 Organização da Equipe

* João Pedro Cabral → responsável pelos dados brutos
* Gabriel Bezerra → responsável pela limpeza e transformação
* Mateus Anchieta → responsável pelos insights e visualizações

---

## 📌 Status do Projeto

🚧 Em desenvolvimento inicial

---

## 📎 Observações

* Os dados em `data/raw/` não devem ser modificados
* Todo desenvolvimento deve ser feito via branches e Pull Requests
* Estrutura pensada para ser simples e escalável
