import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv(r"C:\Users\Gabriela Martins\OneDrive\Ebac\Python\ecommerce_estatistica.csv.csv")
print(df.head().to_string())

# Gráfico Histograma
plt.figure(figsize=(10,6))
plt.hist(df['Preco'], bins=20)
plt.xlabel('Preço')
plt.ylabel('Frequência')
plt.title('Distribuição dos preços')
plt.grid(True)
plt.show()

# Gráfico de dispersão

plt.figure(figsize=(10,6))
plt.scatter(df['Preco'], df['Qtd_Vendidos_Cod'], alpha=0.6)
plt.title('Preço x Quantidade Vendida')
plt.xlabel('Preço')
plt.ylabel('Quantidade Vendida')
plt.show()

# Mapa de calor

df_corr = df.select_dtypes(include='number').corr()
plt.figure(figsize=(10,6))
sns.heatmap(df_corr, annot=True, fmt=".2f")
plt.title('Mapa de Correlação')
plt.show()

# Gráfico de barra

plt.figure(figsize=(10,6))
df['Marca'].value_counts().plot(kind='bar')
plt.title('Quantidade de Produtos por Marca')
plt.xlabel('Marca')
plt.ylabel('Quantidade')
plt.show()

# Gráfico de Pizza

plt.figure(figsize=(10,6))
df['Genero'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Distribuição por Gênero')
plt.ylabel('')
plt.show()

# Gráfico de Densidade

plt.figure(figsize=(10,6))
sns.kdeplot(df['Preco'])
plt.title('Densidade de Preços')
plt.xlabel('Preço')
plt.show()

# Gráfico de Regressão

plt.figure(figsize=(10,6))
sns.regplot(x='Preco', y='Qtd_Vendidos_Cod', data=df)
plt.title('Regressão: Preço x Quantidade Vendida')
plt.show()

