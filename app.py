import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

def prepareFile():

    np = file['nuovi_positivi']
    t = file['tamponi']
    deltaP = []
    for i in range(len(np)):
        if i == 0:
            delta = float(np[i])*100/float(t[i])
        else:
            delta = float(np[i])*100/float(t[i] - t[i-1])

        deltaP.append(delta)
    file['positivi_normalizzati'] = deltaP

    x = file['deceduti']
    deltaD = []
    for i in range(len(x)):
        if i == 0:
            delta = 0
        else:
            delta = x[i] - x[i-1]
        deltaD.append(delta)
    file['delta_deceduti'] = deltaD




external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
file = pd.read_csv('https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv')
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

prepareFile()

lista=["positivi_normalizzati", "totale_casi", "nuovi_positivi", "ricoverati_con_sintomi", "deceduti", "delta_deceduti"]

app.layout = html.Div([
    html.Div([

        html.Div([
            dcc.Dropdown(
                id='yaxis-column',
                options=[{'label': i, 'value': i} for i in lista],
                value='nuovi_positivi'
            ),

        ],)
    ]),

    dcc.Graph(id='indicator-graphic'),

])

@app.callback(
    Output('indicator-graphic', 'figure'),
    [Input('yaxis-column', 'value')])
def update_graph(yaxis_column_name):


    fig = px.bar(y=file[yaxis_column_name], x=file['data'])
    fig.update_xaxes(fixedrange=True)
    fig.update_yaxes(fixedrange=True)
    #fig = px.scatter(x=dff[dff['data'] == xaxis_column_name]['Value'],y=dff[dff['Indicator Name'] == yaxis_column_name]['Value'], hover_name=dff[dff['Indicator Name'] == yaxis_column_name]['Country Name'])

    #fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')

    return fig

if __name__ == "__main__":
    app.run_server(debug=True)
