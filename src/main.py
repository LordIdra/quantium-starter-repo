from venv import create
import pandas
import plotly.express as px
import plotly.graph_objects as go
import dash


path = "data.csv"
data = pandas.read_csv(path)


def data_by_branch(branch):
    return data[data.branch.eq(branch)]


def plot_branch(branch):
    return px.line(
        data_by_branch(branch), 
        x="date", 
        y="sales", )
    

def plot_all_branches():
    return px.line(
        data, 
        x="date", 
        y="sales",
        color="branch")


def apply_style(graph):
    #graph.update_layout(paper_bgcolor="#3f3f3f")
    #graph.update_layout(legend_title_font_color="#ffffff")
    #graph.update_layout(font_color="#ffffff")
    graph.update_layout(
        {
            "title": {
                "text": "Pink Morsel sales over time",
                "font": {
                    "color": "#ffffff"
                }
            },
            "font": {
                "color": "#ffffff"
            },
            "paper_bgcolor": "#202020",
            "plot_bgcolor": "#202020"
        }
    )
    graph.update_traces(line_width=1)
    graph.update_xaxes(linecolor='#808080', gridcolor='#606060')
    graph.update_yaxes(linecolor='#808080', gridcolor='#606060')
    return graph


def create_app():
    app = dash.Dash(__name__)
    app.layout = dash.html.Div(children=[
    dash.html.H1(
        "DATA VISUALISATION YAY",
        id="header"),
    dash.dcc.Graph(
        id="main-graph",
        figure=plot_all_branches()),
    dash.dcc.RadioItems(
        id="branch-select",
        options = ['North', 'East','South', 'West', 'All'], 
        value="North")])

    @app.callback(
        dash.Output(component_id='main-graph', component_property='figure'),
        dash.Input(component_id='branch-select', component_property='value')
    )
    def update(input_value):
        if input_value == "All":
            return apply_style(plot_all_branches())
        else:
            return apply_style(plot_branch(input_value.lower()))
    
    return app


def run_app(app):
    app.run_server(debug=True)

if __name__ == "__main__":
    run_app(create_app())