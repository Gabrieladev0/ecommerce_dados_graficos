# 🛒 E-commerce — Análise Estatística e Dashboard Interativo

Projeto de análise exploratória de dados de e-commerce com visualizações estáticas e um dashboard interativo, desenvolvido em **Python**.

---

## 📁 Estrutura do Projeto

```
📦 ecommerce-dados-graficos/
 ┣ 📊 ecommerce_estatistica.csv     # Dataset com 494 produtos
 ┣ 📄 ecommerce_estatistica.py      # Análise estatística com gráficos estáticos
 ┗ 📄 visualizacao_interativa.py    # Dashboard interativo com Dash + Plotly
```

---

## 📋 Sobre o Dataset

O arquivo `ecommerce_estatistica.csv` contém dados de produtos de moda masculina e feminina com as seguintes informações:

| Coluna             | Descrição                              |
|--------------------|----------------------------------------|
| `Titulo`           | Nome do produto                        |
| `Nota`             | Avaliação média (0–5)                  |
| `N_Avaliacoes`     | Número de avaliações                   |
| `Desconto`         | Percentual de desconto                 |
| `Marca`            | Marca do produto                       |
| `Material`         | Material do produto                    |
| `Genero`           | Público-alvo (Masculino/Feminino)      |
| `Temporada`        | Temporada de uso                       |
| `Qtd_Vendidos`     | Quantidade vendida                     |
| `Preco`            | Preço do produto                       |
| `Review1/2/3`      | Avaliações escritas dos clientes       |

---

## 📚 Conteúdo por Arquivo

### `ecommerce_estatistica.py` — Análise Estática
Gráficos gerados com **Matplotlib** e **Seaborn**:

- 📊 **Histograma** — Distribuição dos preços
- 🔵 **Dispersão** — Preço x Quantidade Vendida
- 🌡️ **Mapa de Calor** — Correlação entre variáveis numéricas
- 📊 **Barras** — Quantidade de produtos por marca
- 🥧 **Pizza** — Distribuição por gênero
- 〰️ **Densidade** — Distribuição de preços (KDE)
- 📈 **Regressão** — Relação entre preço e quantidade vendida

### `visualizacao_interativa.py` — Dashboard Interativo
Dashboard web com **Dash** e **Plotly**:

- ✅ **Checklist** para filtrar por marca
- 📊 **Gráfico de barras** — Marca por Preço (atualizado dinamicamente)
- 🌐 **Gráfico 3D** — Preço x Quantidade Vendida x Nota (interativo)

---

## 🚀 Como executar

### Pré-requisitos

```bash
pip install pandas matplotlib seaborn plotly dash
```

### Rodar a análise estática

```bash
python ecommerce_estatistica.py
```

### Rodar o dashboard interativo

```bash
python visualizacao_interativa.py
```

Depois abra no navegador: [http://localhost:8050](http://localhost:8050)

> ⚠️ **Atenção:** antes de rodar, atualize o caminho do CSV nos arquivos `.py` para o caminho correto na sua máquina:
> ```python
> df = pd.read_csv("ecommerce_estatistica.csv")
> ```

---

## 💡 Exemplo de visualização gerada

```python
# Mapa de correlação entre variáveis numéricas
df_corr = df.select_dtypes(include='number').corr()
sns.heatmap(df_corr, annot=True, fmt=".2f")
plt.title('Mapa de Correlação')
plt.show()
```

---

## 🛠️ Tecnologias

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=python&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-4C72B0?style=for-the-badge&logo=python&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![Dash](https://img.shields.io/badge/Dash-008DE4?style=for-the-badge&logo=plotly&logoColor=white)

---

## 📝 Licença

Este projeto é de uso educacional e está sob a licença MIT.
