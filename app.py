import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import os

#per le regioni crea la lista con i dati solo per quella regione
def removeIncorrectLines(list, name):

    list = list[list.denominazione_regione == name]
    list.reset_index(drop=True, inplace = True)
    return list

#aggiunge le colonne dei positivi normalizzati, delta deceduti
def prepareFile(lista):

    np = lista['nuovi_positivi']
    t = lista['tamponi']
    deltaP = []
    for i in range(len(t)):
        if t[i] != 0:
            if i == 0:
                delta = float(np[i])*100/float(t[i])
            else:
                if (t[i] - t[i-1]) != 0:
                    delta = float(np[i])*100/float(t[i] - t[i-1])
                else:
                    delta = 0
        else:
            delta = 0

        if(delta > 100 ) or (delta < 0):
            delta  = 0
            
        deltaP.append(delta)

    lista['positivi_normalizzati'] = deltaP

    x = lista['deceduti']
    deltaD = []
    for i in range(len(x)):
        if i == 0:
            delta = 0
        else:
            delta = x[i] - x[i-1]
        deltaD.append(delta)
    lista['delta_deceduti'] = deltaD

    return lista

#crea il dizionario con il file associato ad ogni regione
def prepareFileRegioni():

    regioni = {
        "Abruzzo": pd.read_csv('https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni.csv'),
        "Basilicata": pd.read_csv('https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni.csv'),
        "Calabria": pd.read_csv('https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni.csv'),
        "Campania": pd.read_csv('https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni.csv'),
        "Emilia-Romagna": pd.read_csv('https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni.csv'),
        "Friuli Venezia Giulia": pd.read_csv('https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni.csv'),
        "Lazio": pd.read_csv('https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni.csv'),
        "Liguria": pd.read_csv('https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni.csv'),
        "Lombardia": pd.read_csv('https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni.csv'),
        "Marche": pd.read_csv('https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni.csv'),
        "Molise": pd.read_csv('https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni.csv'),
        "P. A. Bolzano": pd.read_csv('https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni.csv'),
        "P. A. Trento": pd.read_csv('https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni.csv'),
        "Piemonte": pd.read_csv('https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni.csv'),
        "Puglia": pd.read_csv('https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni.csv'),
        "Sardegna": pd.read_csv('https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni.csv'),
        "Sicilia": pd.read_csv('https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni.csv'),
        "Toscana": pd.read_csv('https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni.csv'),
        "Umbria": pd.read_csv('https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni.csv'),
        "Valle d'Aosta": pd.read_csv('https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni.csv'),
        "Veneto": pd.read_csv('https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni.csv')
    }

    for i in listaNomiRegioni:
        regioni[i] = removeIncorrectLines(regioni[i], i)
        regioni[i] = prepareFile(regioni[i])
    return regioni

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
file = pd.read_csv('https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv')
fileRegioni = pd.read_csv('https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni.csv')

lista=["positivi_normalizzati", "totale_casi", "nuovi_positivi", "ricoverati_con_sintomi", "deceduti", "delta_deceduti"]
listaNomiRegioni = [
                    "Abruzzo",
                    "Basilicata",
                    "Calabria",
                    "Campania",
                    "Emilia-Romagna",
                    "Friuli Venezia Giulia",
                    "Lazio",
                    "Liguria",
                    "Lombardia",
                    "Marche",
                    "Molise",
                    "P. A. Bolzano",
                    "P. A. Trento",
                    "Piemonte",
                    "Puglia",
                    "Sardegna",
                    "Sicilia",
                    "Toscana",
                    "Umbria",
                    "Valle d'Aosta",
                    "Veneto"
                    ]

listaNomiRegioniConTotale = [
                    "Abruzzo",
                    "Basilicata",
                    "Calabria",
                    "Campania",
                    "Emilia-Romagna",
                    "Friuli Venezia Giulia",
                    "Lazio",
                    "Liguria",
                    "Lombardia",
                    "Marche",
                    "Molise",
                    "P. A. Bolzano",
                    "P. A. Trento",
                    "Piemonte",
                    "Puglia",
                    "Sardegna",
                    "Sicilia",
                    "Toscana",
                    "Umbria",
                    "Valle d'Aosta",
                    "Veneto",
                    "italia"
                    ]


file = prepareFile(file)
print("file preparato")
regioni = prepareFileRegioni()
print("file regioni preparato")

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Div([

        html.Div([
            dcc.Dropdown(
                id='yaxis-column',
                options=[{'label': i, 'value': i} for i in lista],
                value='positivi_normalizzati'
            ),

        ],),

        html.Div([
            dcc.Dropdown(
                id='regione',
                options=[{'label': i, 'value': i} for i in listaNomiRegioniConTotale],
                value='italia'
            ),

        ],)
    ]),

    dcc.Graph(id='indicator-graphic'),

])

@app.callback(
    Output('indicator-graphic', 'figure'),
    [Input('yaxis-column', 'value'),
     Input('regione', 'value')])
def update_graph(yaxis_column_name, region):

    if(region == 'italia'):

        fig = px.bar(y=file[yaxis_column_name], x=file['data'])
        fig.update_xaxes(fixedrange=True)
        fig.update_yaxes(fixedrange=True)
    else:
        fig = px.bar(y=regioni[region][yaxis_column_name], x=regioni[region]['data'])
        fig.update_xaxes(fixedrange=True)
        fig.update_yaxes(fixedrange=True)
    #fig = px.scatter(x=dff[dff['data'] == xaxis_column_name]['Value'],y=dff[dff['Indicator Name'] == yaxis_column_name]['Value'], hover_name=dff[dff['Indicator Name'] == yaxis_column_name]['Country Name'])

    #fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')

    return fig

if __name__ == "__main__":
    app.run_server(debug=True)
