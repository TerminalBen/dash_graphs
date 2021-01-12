import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import consumo_eletrico_data as ed

external_stylesheets1 = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
years=[2016,2017,2018,2019,2020]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets1)
server = app.server

app.layout = html.Div(children=[
    html.H1(children='Apuramento Faturas Eletricidade'),

    html.Div(children='''
        Valores em Kilowatts
    '''),
    

    dcc.Graph(
        id='MS',
        figure={
            'data': [
                {'x': ed.year, 'y': ed.ms2017,
                    'type': 'bar', 'name': '2017'},
                {'x': ed.year, 'y': ed.ms2018,
                    'type': 'bar', 'name': '2018'},
                {'x': ed.year, 'y': ed.ms2019,
                    'type': 'bar', 'name': '2019'},
                {'x': ed.year, 'y': ed.ms2020,
                    'type': 'bar', 'name': '2020'},
            ],
            'layout': go.Layout( 
                title='Monte Sossego Rua 1',
                yaxis={'title': 'Valores em Kw'},
                colorway = ['#ff7f0e', '#2ca02c', '#d62728', '#9467bd'],
            ),
        }
    ),

    dcc.Graph(
        id='sum_ms',
        figure={
            'data': [go.Pie(labels=['2017','2018', '2019','2020'], values=[ed.s1, ed.s2, ed.s3,ed.sms2020], hole=0.3,sort=False)],
            'layout': go.Layout( 
                title='Comparação Anual',
                #yaxis={'title': 'Valores em Kw'},
                colorway = ['#ff7f0e', '#2ca02c', '#d62728', '#9467bd'],
            ),
            
        }
        #figure.update_traces(textinfo='value')
    ),

    dcc.Graph(
        id='Camp',
        figure={
            'data': [
                {'x': ed.year, 'y': ed.camp2016,
                    'type':'bar','name': '2016'},
                {'x': ed.year, 'y': ed.camp2017,
                    'type': 'bar', 'name': '2017'},
                {'x': ed.year, 'y': ed.camp2018,
                    'type': 'bar', 'name': '2018'},
                {'x': ed.year, 'y': ed.camp2019,
                    'type': 'bar', 'name': '2019'},
                {'x': ed.year, 'y': ed.camp2020,
                    'type': 'bar', 'name': '2020'},
            ],
            'layout': go.Layout (
                title='Consumo Eletricidade Campinho',
                yaxis={'title':'Valores em Kw (x1000)'},
                
            )
        }
    ),

    
    #html.Div([
     #   html.P ('Valores em Kilowats')
      #  ],
       # style = {'textAlign':'left','margin-top':0,'font-size':11}
    #),
    

    html.Div([
        html.P ('Inicio funcionamento Painel solar em 03 de Setembro de 2018'),
        html.P ('Arranque das camaras Frigorificas em 01 de Maio de 2018')
        ],
        style = {'textAlign':'right','margin-top':0.5,'font-size':11}
    ),

    dcc.Graph(
        id='sum_camp',
        figure={
            'data': [go.Pie(labels=['2016','2017','2018', '2019','2020'], values=[ed.scamp2016,ed.s4, ed.s5, ed.s6,ed.scamp2020], hole=0.3,sort=False)],
            'layout': {'title': 'Comparação Anual'}
        }
    ),

    dcc.Graph(
        id='sj',
        figure={
            'data': [
                {'x': ed.year, 'y': ed.sj2018,
                    'type': 'bar', 'name': '2018'},
                {'x': ed.year, 'y': ed.sj2019,
                    'type': 'bar', 'name': '2019'},
                {'x': ed.year, 'y': ed.sj2020,
                    'type': 'bar', 'name': '2020',
                    },
            ],
            'layout': go.Layout( 
                title='Minimercado Rua São João',
                yaxis={'title': 'Valores em Kw'},
                colorway = ['#2ca02c', '#d62728', '#9467bd'],
            )
        }
    ),
    
    html.Div([
    html.P ('Colocação painel solar  26 de Agosto de 2018'),
    ],
    style = {'textAlign':'right','margin-top':1,'font-size':11}),

    dcc.Graph(
        id='sum_sj',
        figure={
            'data': [go.Pie(labels=['2018', '2019','2020'], values=[ed.s8, ed.s9,ed.ssj2020], hole=0.3,sort=False)],
            'layout': {'title': 'Comparação Anual','colorway':['#2ca02c', '#d62728', '#9467bd']}
        }
    ),

    dcc.Graph(
        id='escr_cid',
        figure={
            'data': [
                {'x': ed.year, 'y': ed.ec2016,
                    'type':'bar','name':'2016'},
                {'x': ed.year, 'y': ed.ec2017,
                    'type': 'bar', 'name': '2017'},
                {'x': ed.year, 'y': ed.ec2018,
                    'type': 'bar', 'name': '2018'},
                {'x': ed.year, 'y': ed.ec2019,
                    'type': 'bar', 'name': '2019'},
                {'x': ed.year, 'y': ed.ec2020,
                    'type': 'bar', 'name': '2020'},
            ],
            'layout': go.Layout (
                title='Consumo eletricidade Posto de Venda/Escritório',
                yaxis={'title':'Valores em Kw'},
                xaxis={'title':'Paineis Solares em funcionamento a partir de 31 de Março de 2017'}
            )
        }
    ),

    html.Div([
        html.P ('Paineis Solares em funcionamento a partir de 31 de Março de 2017'),
        html.P ('Junçao de Contadores Posto de Venda/Escritorio em 14 de Julho de 2018')
        ],
        style = {'textAlign':'right','margin-top':0.5,'font-size':11}
    ),
    
    dcc.Graph(
        id='sum_cid',
        figure={
            'data': [go.Pie(labels=['2016','2017','2018', '2019','2020'], values=[ed.sumec2016,ed.sumec2017, ed.sumec2018, ed.sumec2019,ed.sec2020], hole=0.3,sort=False)],
            'layout': {'title': 'Comparação Anual','colorway':[]}
        }
    ),

    dcc.Graph(
        id='rib',
        figure={
            'data': [
                {'x': ed.year, 'y': ed.rib2017,
                    'type': 'bar', 'name': '2017'},
                {'x': ed.year, 'y': ed.rib2018,
                    'type': 'bar', 'name': '2018'},
                {'x': ed.year, 'y': ed.rib2019,
                    'type': 'bar', 'name': '2019'},
                {'x': ed.year, 'y': ed.rib2020,
                    'type': 'bar', 'name': '2020'},
            ],
            'layout': go.Layout( 
                title='Ribeirinha',
                yaxis={'title': 'Valores em Kw'},
                colorway = ['#ff7f0e', '#2ca02c', '#d62728', '#9467bd'],
            ),
        }
    ),


     html.Div([
        html.P ('Valores em Kilowats')],
        style = {'textAlign':'right','margin-top':1,'font-size':11}
    ),

    dcc.Graph(
        id='sum_rib',
        figure={
            'data': [go.Pie(labels=['2017', '2018', '2019','2020'], values=[ed.s16, ed.s17, ed.s18,ed.srib2020], hole=0.3,sort=False)],
            'layout': go.Layout( 
                title='Comparação Anual',
                #yaxis={'title': 'Valores em Kw'},
                colorway = ['#ff7f0e', '#2ca02c', '#d62728', '#9467bd'],
            ),
            
        }
    ),
    dcc.Graph(
        id='pn',
        figure={
            'data': [
                {'x': ed.year, 'y': ed.pn2017,
                    'type': 'bar', 'name': '2017'},
                {'x': ed.year, 'y': ed.pn2018,
                    'type': 'bar', 'name': '2018'},
                {'x': ed.year, 'y': ed.pn2019,
                    'type': 'bar', 'name': '2019'},
                {'x': ed.year, 'y': ed.pn2020,
                    'type': 'bar', 'name': '2020'},
            ],
            'layout': go.Layout( 
                title='Porto Novo',
                yaxis={'title': 'Valores em Kw'},
                colorway = ['#ff7f0e', '#2ca02c', '#d62728', '#9467bd'],
            ),
        }
    ),

    html.Div([
    html.P ('Colocação painel solar 29 de Setembro de 2018'),
    html.P ('Valores em Kilowats')
    ],
    style = {'textAlign':'right','margin-top':1,'font-size':11}
    ),

    dcc.Graph(
        id='sum_pn',
        figure={
            'data': [go.Pie(labels=['2017','2018', '2019','2020'], values=[ed.s19, ed.s20, ed.s21,ed.spn2020], hole=0.3,sort=False)],
            'layout': {'title': 'Comparação Anual','colorway':['#ff7f0e', '#2ca02c', '#d62728', '#9467bd']}
        }
    ),
])

if __name__ == '__main__':
    app.run_server(debug=True)

