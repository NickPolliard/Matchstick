import json
import os

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import dapp
from apps import MatchStick
from apps import ManualMatch, KnownPopulation
from apps import page_3, HiddenPage

dapp.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


# UI Page content routes
@dapp.callback(Output('page-content', 'children'),
               [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return MatchStick.layout
    elif pathname == '/MatchStick':
        return MatchStick.layout
    elif pathname == '/ManualMatch':
        return ManualMatch.layout
    elif pathname == '/KnownPopulation':
        return KnownPopulation.layout
    elif pathname == '/page_3':
        return page_3.layout
    elif pathname == '/HiddenPage':
        return HiddenPage.layout
    else:
        return '404: Page not found'


# Traditional API routes
@dapp.server.route("/ping")
def ping():
    return "{status: ok}"


@dapp.server.route("/version")
def version():
    with open('version.json') as json_file:
        data = json.load(json_file)
    return data


# start Flask server
if __name__ == '__main__':
    if os.environ.get('ENVIRONMENT') == 'dev':
        debug = True
    else:
        debug = False

    print('Run server')
    dapp.run_server(
        debug=debug,
        host='0.0.0.0',
        port=8050
    )
