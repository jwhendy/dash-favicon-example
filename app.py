import dash
import dash_core_components as dcc
import dash_html_components as html
import flask
import os

app = dash.Dash(__name__)
server = app.server

app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

app.layout = html.Div(html.H2('dash favicon example'))

# favicon found here:
# - http://www.iconarchive.com/show/mono-business-2-icons-by-custom-icon-design/thumbs-up-icon.html
@server.route('/favicon.ico')
def favicon():
    return flask.send_from_directory(os.path.join(server.root_path, 'static'),
                                     'favicon.ico')


if __name__ == '__main__':
    app.run_server(debug=True)
