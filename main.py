import plotly.express as px
import pandas as pd

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

def main():

    file = pd.read_csv('https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv')

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
            delta[i] = 0
        else:
            delta[i] = x[i] - x[i-1]
        delpaD.append(delta)
    file['delta_deceduti'] = deltaD

    while True:

        print("Software per la visulizzazione dei dati relativi al COVID-19 in italia:")
        print("0-EXIT")
        print("1-POSIVI NORMALIZZATI AI TAMPONI")
        print("2-TOTALE POSITIVI")
        print("3-NUOVI POSITIVI")
        print("4-TOTALE SINTOMATICI")
        print("5-DECESSI")
        print("6-INCREMENTO DECESSI")
        x = int( input())



        if (x<7 and x >-1):

            if(x == 0):
                break
            if(x == 1):

                fig = px.line(file, x='data', y='positivi_normalizzati')
                fig.show()
            if(x == 2):
                fig = px.line(file, x='data', y='totale_casi')
                fig.show()
            if(x == 3):
                fig = px.line(file, x='data', y='nuovi_positivi')
                fig.show()
            if(x == 4):
                fig = px.line(file, x='data', y='ricoverati_con_sintomi')
                fig.show()
            if(x == 5):
                fig = px.line(file, x='data', y='deceduti')
                fig.show()
            if(x == 6):
                x = file['deceduti']
                delta = []

                for i in range(len(x)):
                    if i == 0:
                        delta[i] = 0
                    else:
                        delta[i] = x[i] - x[i-1]

                fig = px.line(file, x='data', y=delta)
                fig.show()


if __name__ == "__main__":
    main()
