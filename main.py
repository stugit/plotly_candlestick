import plotly.graph_objs as go
import pandas_datareader as web
from datetime import datetime

import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go

df = web.DataReader("aapl", 'morningstar').reset_index()

trace = go.Candlestick(x=df.Date,
                       open=df.Open,
                       high=df.High,
                       low=df.Low,
                       close=df.Close,
                       increasing=dict(line=dict(color= '#17BECF')),
                       decreasing=dict(line=dict(color= '#7F7F7F')))

data = [trace]
fig=dict(data=data, layout=dict(autosize=True, height=700))

app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(
        id='Simple Candlestick Demo',
        figure=fig 
    )
])

if __name__ == '__main__':
    app.run_server(debug=False)
