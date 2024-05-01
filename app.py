from dash import Dash, html, dcc
from  plotly.express import line
import pandas as pd

app = Dash(__name__)


df = pd.read_csv('./output_file.csv')
df = df.sort_values(by="date")
fig = line(df, x="date", y="sales", title='Pink Morsel sales summary')


app.layout = html.Div(children=[
    html.H1(children='Pink Morsel visualiser'),

    

    dcc.Graph(
        id='visualization',
        figure= fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)
