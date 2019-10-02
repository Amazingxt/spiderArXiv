# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import sqlite3

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#228B22',
    'text': '#7FDBFF'
}

readmefile = '本页面用于文得发工作室对广大科研工作者进行arxiv文章推送使用'

app.layout = html.Div([
    html.H1(children='文得发工作室',
            style={
                'textAlign': 'center',
                'color': colors['text']}
            ),
    html.H3(children='使用说明',
            style={
                'textAlign': 'center',
                'color': colors['text']}
            ),
    html.P(children=readmefile,
           style={
               'textAlign': 'center',
               'color': colors['text']}
           ),
    html.Div([
        html.P('姓名'),
        dcc.Input(id='name-box', type='text')
    ],
        style={
        'textAlign': 'center',
    }),
    html.Div([
        html.P('邮箱'),
        dcc.Input(id='email-box', type='text')
    ],
        style={
        'textAlign': 'center',
    }),
    html.Div([
        html.P('专业领域'),
        dcc.Input(id='major-box', type='text')
    ],
        style={
        'textAlign': 'center',
    }),
    html.Div([
        html.P('单位'),
        dcc.Input(id='company-box', type='text')
    ],
        style={
        'textAlign': 'center',
    }),
    html.Div([
        html.P('内容关键词'),
        dcc.Input(id='keywords-box', type='text')
    ],
        style={
        'textAlign': 'center',
    }),
    html.Div([
        html.P('作者关键词'),
        dcc.Input(id='author-box', type='text')
    ],
        style={
        'textAlign': 'center',
    }),
    html.P(' '),
    html.Div([
        html.Button('Submit', id='button', style={
                    "color": colors['text'], 'backgroundColor': colors['background']}),
    ],
        style={
        'textAlign': 'center',

    }),
    html.Div(id='output-container-button',
             children='请填入上面的信息并点击提交', style={'textAlign': 'center', }),
    html.P(' '),
    html.P(' '),
    html.Div([
        html.Img(src="assets/logo.jpg", className="app__logo",
                 style={"width": 300, "height": 300}),
    ],
        style={
        'textAlign': 'center',
    })


])


@app.callback(
    dash.dependencies.Output('output-container-button', 'children'),
    [dash.dependencies.Input('button', 'n_clicks')],
    [dash.dependencies.State('name-box', 'value'),
     dash.dependencies.State('email-box', 'value'),
     dash.dependencies.State('major-box', 'value'),
     dash.dependencies.State('company-box', 'value'),
     dash.dependencies.State('keywords-box', 'value'),
     dash.dependencies.State('author-box', 'value')]
)
def update_output(n_clicks, name, email, major, company, keywords, author):

    conn = sqlite3.connect('personQueryInfo.db')
    c = conn.cursor()

    try:
        c.execute('''create table user_tb(
            _id integer primary key autoincrement,
            keyWords text,
            authors text,
            email text,
            person text,
            company text,
            major text)
            ''')
    except:
        pass

    if keywords == None and author == None and email == None and name == None and company == None and major == None:
        c.close()
        conn.close()
        return '请填入上面的信息并点击提交'
    elif keywords == None or author == None or email == None or name == None or company == None or major == None:
        c.close()
        conn.close()
        return '填写信息不全'

    else:
        c.execute('insert into user_tb values(null, ?, ?, ?, ?, ?, ?)',
                  ((keywords, author, email, name, company, major)))

        conn.commit()

    c.close()
    conn.close()
    return '您已提交成功，请勿重复提交！'


if __name__ == '__main__':
    app.run_server(debug=True)
