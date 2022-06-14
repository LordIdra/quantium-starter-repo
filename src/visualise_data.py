import pandas
import plotly.express as px
import dash


path = "data.csv"
branch = "north"

data = pandas.read_csv(path)
data = data[data.branch.eq(branch)]

fig = px.line(data, x="date", y="sales", title='Pink Morsel sales over time')

app = dash.Dash(__name__)

app.layout = dash.html.Div(children=[
    dash.dcc.Graph(
        id='pink-morsel-graph',
        figure=fig
    )
])

app.run_server()