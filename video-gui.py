from dash import Dash, dcc, html, Input, Output, State, ctx
from dash.dependencies import Input, Output
# import dash_daq as daq
from dash import html
# from jupyter_dash import JupyterDash
from dash import dcc
# import torch
# import numpy as np
# import plotly.graph_objs as go
# import cv2
# from PIL import Image

imagen_links = ["https://imagen.research.google/video/hdvideos/4.mp4",  # leaves
                "https://imagen.research.google/video/hdvideos/28.mp4",  # dishes
                "https://imagen.research.google/video/hdvideos/8.mp4",  # glass
                "https://imagen.research.google/video/hdvideos/55.mp4",  # cathedral
                "https://imagen.research.google/video/hdvideos/25.mp4",  # nyc
                ]
makeavideo_links = ["https://makeavideo.studio/assets/overview.webp",  # hero
                    "https://makeavideo.studio/assets/surreal2.webp",  # robot
                    "https://makeavideo.studio/assets/style1.webp",  # mars
                    "https://makeavideo.studio/assets/real2.webp",  # fish
                    "https://makeavideo.studio/assets/surreal4.webp",  # sloth
                    ]
# divider = Image.open(
#     'C:\\Users\\alexs\\Dropbox (MIT)\\Subjects_Fall2022\\6.S898\\Project\\Code\\Imagen_v_Makeavideo_Videos\\divider.png')

app = Dash(__name__)
server = app.server
app.layout = html.Div([

    # imagen
    html.Video(
        controls=True,
        id='imagen_link',
        src=imagen_links[0],
        autoPlay=True,
        loop=True,
        muted=True,
        style={'position': 'absolute', 'margin-left': 30, 'margin-top': 60, 'width': '350px'}),

    html.H1('Imagen Video',
            style={'position': 'absolute', 'color': '#b5b5b5', 'fontSize': 25, 'margin-left': 120, 'margin-top': 20,
                   'font-family': 'Arial'}),
    html.H1('Select a prompt to generate a new video:',
            style={'position': 'absolute', 'color': '#b5b5b5', 'fontSize': 15, 'margin-left': 60, 'margin-top': 280,
                   'font-family': 'Arial'}),
    html.Button("A bunch of autumn leaves falling on a calm lake to form the text \'Imagen Video\'. Smooth.",
                id='imagen_leaves', n_clicks=0, style={'position': 'absolute', 'margin-left': 30, 'margin-top': 305,
                                                       "backgroundColor": "white", 'border': '1px #616161 solid',
                                                       'height': '40px', 'width': '350px', 'font-family': 'Arial',
                                                       'color': '#616161', 'border-radius': '8px'}),
    html.Button("A teddy bear washing the dishes.", id='imagen_dishes', n_clicks=0,
                style={'position': 'absolute', 'margin-left': 30, 'margin-top': 355,
                       "backgroundColor": "white", 'border': '1px #616161 solid', 'height': '40px', 'width': '350px',
                       'font-family': 'Arial', 'color': '#616161', 'border-radius': '8px'}),
    html.Button("A clear wine glass with turquoise-colored waves inside it.", id='imagen_glass', n_clicks=0,
                style={'position': 'absolute', 'margin-left': 30, 'margin-top': 405,
                       "backgroundColor": "white", 'border': '1px #616161 solid', 'height': '40px', 'width': '350px',
                       'font-family': 'Arial', 'color': '#616161', 'border-radius': '8px'}),
    html.Button("Drone flythrough interior of Sagrada Familia cathedral.", id='imagen_cathedral', n_clicks=0,
                style={'position': 'absolute', 'margin-left': 30, 'margin-top': 455,
                       "backgroundColor": "white", 'border': '1px #616161 solid', 'height': '40px', 'width': '350px',
                       'font-family': 'Arial', 'color': '#616161', 'border-radius': '8px'}),
    html.Button("A teddy bear running in New York City.", id='imagen_nyc', n_clicks=0,
                style={'position': 'absolute', 'margin-left': 30, 'margin-top': 505,
                       "backgroundColor": "white", 'border': '1px #616161 solid', 'height': '40px', 'width': '350px',
                       'font-family': 'Arial', 'color': '#616161', 'border-radius': '8px'}),
    # make-a-video
    html.Img(
        # controls = False,
        id='makeavideo_link',
        src=makeavideo_links[0],
        # autoPlay=True,
        # loop=True,
        style={'position': 'absolute', 'margin-left': 515, 'margin-top': 60, 'width': '210px'}),

    html.H1('Make-a-Video',
            style={'position': 'absolute', 'color': '#b5b5b5', 'fontSize': 25, 'margin-left': 540, 'margin-top': 20,
                   'font-family': 'Arial'}),
    html.H1('Select a prompt to generate a new video:',
            style={'position': 'absolute', 'color': '#b5b5b5', 'fontSize': 15, 'margin-left': 475, 'margin-top': 280,
                   'font-family': 'Arial'}),
    html.Button("A dog wearing a Superhero outfit with red cape flying through the sky.", id='make_hero', n_clicks=0,
                style={'position': 'absolute', 'margin-left': 450, 'margin-top': 305,
                       "backgroundColor": "white", 'border': '1px #616161 solid', 'height': '40px', 'width': '350px',
                       'font-family': 'Arial', 'color': '#616161', 'border-radius': '8px'}),
    html.Button("Robot dancing in times square.", id='make_robot', n_clicks=0,
                style={'position': 'absolute', 'margin-left': 450, 'margin-top': 355,
                       "backgroundColor": "white", 'border': '1px #616161 solid', 'height': '40px', 'width': '350px',
                       'font-family': 'Arial', 'color': '#616161', 'border-radius': '8px'}),
    html.Button("Hyper-realistic spaceship landing on mars.", id='make_mars', n_clicks=0,
                style={'position': 'absolute', 'margin-left': 450, 'margin-top': 405,
                       "backgroundColor": "white", 'border': '1px #616161 solid', 'height': '40px', 'width': '350px',
                       'font-family': 'Arial', 'color': '#616161', 'border-radius': '8px'}),
    html.Button("Clown fish swimming through the coral reef.", id='make_fish', n_clicks=0,
                style={'position': 'absolute', 'margin-left': 450, 'margin-top': 455,
                       "backgroundColor": "white", 'border': '1px #616161 solid', 'height': '40px', 'width': '350px',
                       'font-family': 'Arial', 'color': '#616161', 'border-radius': '8px'}),
    html.Button(
        "A fluffy baby sloth with an orange knitted hat trying to figure out a laptop close up highly detailed studio lighting screen reflecting in its eye.",
        id='make_sloth', n_clicks=0, style={'position': 'absolute', 'margin-left': 450, 'margin-top': 505,
                                            "backgroundColor": "white", 'border': '1px #616161 solid', 'height': '60px',
                                            'width': '350px', 'font-family': 'Arial', 'color': '#616161',
                                            'border-radius': '8px'}),

    # html.Img(src=divider, style={'position': 'absolute', 'margin-left': 418, 'margin-top': 60, 'width': '1px'}),

])


@app.callback(
    Output('imagen_link', 'src'),
    Output('makeavideo_link', 'src'),
    Input('imagen_leaves', 'n_clicks'),
    Input('imagen_dishes', 'n_clicks'),
    Input('imagen_glass', 'n_clicks'),
    Input('imagen_cathedral', 'n_clicks'),
    Input('imagen_nyc', 'n_clicks'),

    Input('make_hero', 'n_clicks'),
    Input('make_robot', 'n_clicks'),
    Input('make_mars', 'n_clicks'),
    Input('make_fish', 'n_clicks'),
    Input('make_sloth', 'n_clicks'),

)
def update_output(i1, i2, i3, i4, i5,
                  m1, m2, m3, m4, m5):
    x = 0
    if "imagen_leaves" == ctx.triggered_id:
        x = 0
    elif "imagen_dishes" == ctx.triggered_id:
        x = 1
    elif "imagen_glass" == ctx.triggered_id:
        x = 2
    elif "imagen_cathedral" == ctx.triggered_id:
        x = 3
    elif "imagen_nyc" == ctx.triggered_id:
        x = 4

    y = 0
    if "make_hero" == ctx.triggered_id:
        y = 0
    elif "make_robot" == ctx.triggered_id:
        y = 1
    elif "make_mars" == ctx.triggered_id:
        y = 2
    elif "make_fish" == ctx.triggered_id:
        y = 3
    elif "make_sloth" == ctx.triggered_id:
        y = 4

    im_link = str(imagen_links[x])
    make_link = str(makeavideo_links[y])
    return im_link, make_link


if __name__ == '__main__':
    app.run_server(debug=False)
