from .template.sidebar import *
from .template.navbar import *
from .template.content import *
from .template.footer import *
from .template.callbacks import *

import os
import plotly.express as px

# folder_path = os.path.abspath(os.path.dirname(__file__))
DATA_DIRECTORY = os.path.join(os.path.abspath(
    os.path.dirname(os.path.dirname(__file__))), 'data')
# Create a color scale for the continents
COLOR_SCALE94 = px.colors.named_colorscales() 
COLOR_SCALE10 = px.colors.qualitative.G10 #px.colors.sequential.Plasma