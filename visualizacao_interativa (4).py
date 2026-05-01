from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

# Leitura do CSV
df = pd.read_csv(r"C:\Users\Gabriela Martins\OneDrive\Ebac\Python\ecommerce_estatistica.csv.csv")
print(df.head().to_string())

# Checklist
lista_marca = df['Marca'].unique()
options = [{'label': marca, 'value': marca} for marca in lista_marca]

# Função que cria os gráficos
def cria_grafico(selecionar_marca):

    if not selecionar_marca:
        selecionar_marca = lista_marca

    filtro_df = df[df['Marca'].isin(selecionar_marca)]

    # Gráfico de barras
    fig1 = px.bar(
        filtro_df,
        x='Preco',
        y='Marca',
        color='Marca',
        barmode='group',
        title='Marca por Preço'
    )

    fig1.update_layout(
        xaxis_title='Preço',
        yaxis_title='Marca',
        plot_bgcolor='white',
        paper_bgcolor='white'
    )

    # Gráfico 3D (AGORA CORRETO)
    fig2 = px.scatter_3d(
        filtro_df,
        x='Preco',
        y='Qtd_Vendidos_Cod',
        z='Nota',
        color='Marca',
        title='Preço x Quantidade x Nota'
    )

    fig2.update_layout(
        scene=dict(
            xaxis_title='Preço',
            yaxis_title='Quantidade Vendida',
            zaxis_title='Nota'
        )
    )

    return fig1, fig2

# Função que cria o app
def cria_app():
    app = Dash(__name__)

    app.layout = html.Div([
        html.H1('Dashboard Interativo Ecommerce'),
        html.P('Interatividade entre os dados'),
        html.Br(),

        html.H2('Gráficos'),

        dcc.Checklist(
            id='id_selecionar_marca',
            options=options,
            value=[lista_marca[0]],
            inline=True
        ),

        dcc.Graph(id='id_grafico_barra'),
        dcc.Graph(id='id_grafico_3d'),
    ])

    @app.callback(
        Output('id_grafico_barra', 'figure'),
        Output('id_grafico_3d', 'figure'),
        Input('id_selecionar_marca', 'value')
    )
    def atualizar_graficos(selecionar_marca):
        return cria_grafico(selecionar_marca)

    return app

# Executa o app
if __name__ == '__main__':
    app = cria_app()
    app.run(debug=True, port=8050)
