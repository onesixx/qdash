import pandas as pd
import numpy as np
import os

import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

from alyxdash import DATA_DIRECTORY
from alyxdash.utils import make_pdata_undup

import pickle

dataPath = DATA_DIRECTORY+'/issue_02'
dataPath_pre = dataPath+'_pre'

with open(os.path.join(dataPath_pre, 'proc_01_fch3.pickle'), 'rb') as f:
    fch3 = pickle.load(f)
with open(os.path.join(dataPath_pre, 'proc_01_pch1.pickle'), 'rb') as f:
    pch1 = pickle.load(f)
with open(os.path.join(dataPath_pre, 'proc_01_pch2.pickle'), 'rb') as f:
    pch2 = pickle.load(f)

#TEST --------------------------------------------------------------






# Plotly Express ----------------------------------------------------
pdata = make_pdata_undup(pch2['data'], 'ch01_vol')
fig = px.scatter(pdata,
                 x="time", y="ch01_vol")
fig.show()

# Graph Objects -----------------------------------------------------
pdata = make_pdata_undup(pch2['data'], 'ch01_vol')
trace1 = go.Scatter(
    x=pdata.time,
    y=pdata.ch01_vol,
    mode='markers',
    marker=dict(size=0.2, color="red"),
    line=dict(color='gray')
)
data = [trace1]
layout = go.Layout(yaxis_title="ch01_vol" )
fig = go.Figure(data, layout)
fig.show()

# Graph Objects -----------------------------------------------------

vol_by_channel56 = [f'ch{i+1:02d}_vol' for i in range(56)]
dd = pch2['data']
dd_vol = dd[vol_by_channel56]
dd_vol.transpose()
dd = dd.set_index('time')
# vol_by_channel56 = [f'ch{i+1:02d}_vol' for i in range(56)]
vol_by_channel6 = [f'ch{i+1:02d}_vol' for i in range(2)]
traces = []
# colors = ['blue', 'green', 'red', 'orange',
#           'purple', 'yellow', 'black']  # list of colors to be used
colors = px.colors.qualitative.G10
dd = dd.loc['0000:35:15':]
for i, col_vol in enumerate(vol_by_channel56):
    # col_vol = 'ch01_vol'
    print(f"kkkkk: {i % len(colors)}")
    pdata = make_pdata_undup(dd, col_vol, part=True)
    pdata = pdata.sort_index()
    print(len(colors))
    traces.append(
        go.Scatter(
            x=pdata.index,
            y=pdata[col_vol],
            mode='lines',
            # marker=dict(size=0.2),
            # select color based on index using modulus operator
            line=dict(color=colors[i % len(colors)])
        )
    )
data = traces
layout = go.Layout(template="plotly_white", title="")
fig = go.Figure(data, layout)
fig.show()


df = px.data.gapminder()
df = df.loc[range(30)]
fig = px.line(
    data_frame=df,
    y="lifeExp", x="year",
    color="continent",
    line_group="country",
    line_shape="spline",
    render_mode="static",  # "svg","webgl",
    color_discrete_sequence=px.colors.qualitative.G10,
    title="Built-in G10 color sequence"
)
fig.show()


# Create a color scale for the continents
color_scale = px.colors.qualitative.G10

conti = df['continent'].unique()
dict(color=conti[i % len(conti)])

color[keys[i]]  = [ = conti[i] for i in range(len(conti))]

traces = []
# Add the traces for each country
for country in df['country'].unique():
    data = df[df['country'] == country]
    traces.append(
        go.Scatter(
            x=data['year'],
            y=data['lifeExp'],
            name=country,
            mode='lines',
            line=dict(
                shape='spline',
                # color=color_scale[df[df['country'] == country]['continent'].unique()[0]]
            )
        )
    )
data = traces
layout = go.Layout(title="Built-in G10 color sequence",
                   xaxis_title="Year", yaxis_title="Life Expectancy",
                   colorway=color_scale)
# Create the plotly figure
fig = go.Figure(data, layout)
fig.show()



import plotly.express as px
import numpy as np
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

dd = pch2['data']
dd_vol = dd[vol_by_channel56]
dd_vol_t = dd_vol.transpose()
data_norm = (dd_vol_t - np.mean(dd_vol_t, axis=0)) / np.std(dd_vol_t, axis=0)

pca = PCA(n_components=56)
data_pca = pca.fit_transform(data_norm)

tsne = TSNE(n_components=3)
data_tsne = tsne.fit_transform(data_pca)

vol_channel56 = [f'ch{i+1:02d}_vol' for i in range(56)]

colors = np.linspace(0, 1, 56)

fig = px.scatter_3d(
    data_tsne,
    x=data_tsne[:,0], y=data_tsne[:,1], z=data_tsne[:,2],
    color=vol_channel56
)
fig.show()

T1 = 28+11

t = np.linspace(0, 10, 50)
x, y, z = np.cos(t), np.sin(t), t

trace = go.Scatter3d(x=x, y=y, z=z,
                   mode='markers')

fig = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z,
                                   mode='markers')])
fig.show()


myPalette = px.colors.qualitative.Alphabet
traces = []
traces.append(
    go.Scatter3d(
        x=data_tsne[:, 0], y=data_tsne[:, 1], z=data_tsne[:, 2],
        mode='markers',
        marker=dict(
            size=3,
            color=[myPalette[i % len(myPalette)] for i, col_vol in enumerate(dd_vol_t.index)],
            colorscale='Viridis',   # choose a colorscale
            opacity=0.8,
        )
    )
)
fig.update_traces(hovertemplate=None)
fig.update_layout(hovermode="x")

layout = go.Layout()
fig = go.Figure(traces, layout)
fig.show()
