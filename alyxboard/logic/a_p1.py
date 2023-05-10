# xhttps://github.com/plotly/dash-sample-apps/tree/main/apps/dash-tsne

import pandas as pd
import numpy as np
import os

import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

from cathydash import DATA_DIRECTORY, COLOR_SCALE10
from cathydash.utils import make_pdata_undup

import pickle

from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler, Normalizer
from sklearn.decomposition import PCA


dataPath = DATA_DIRECTORY+'/issue_02'
dataPath_pre = dataPath+'_pre'

with open(os.path.join(dataPath_pre, 'proc_01_fch3.pickle'), 'rb') as f:
    fch3 = pickle.load(f)
with open(os.path.join(dataPath_pre, 'proc_01_pch1.pickle'), 'rb') as f:
    pch1 = pickle.load(f)
with open(os.path.join(dataPath_pre, 'proc_01_pch2.pickle'), 'rb') as f:
    pch2 = pickle.load(f)


df = fch3['data']
# df.columns
df = df.set_index('time')

df_fch3_vol = df.loc[:, [f'ch{i+1:02d}_vol' for i in range(56)]]
df_fch3_curr= df.loc[:, [f'ch{i+1:02d}_curr' for i in range(56)]]
df_fch3_q   = df.loc[:, [f'ch{i+1:02d}_q' for i in range(56)]]
df_fch3_pv  = df.loc[:, [f'ch{i+1:02d}_pv' for i in range(56)]]



dd = df_fch3_vol.loc['0000:03:15':]
# dd = df_fch3_vol

scaler = StandardScaler()
scaler.fit(dd)

X_scaled = scaler.transform(dd)
X_scaled = pd.DataFrame(data=X_scaled, columns=dd.columns)
X_scaled.index = dd.index
print(X_scaled)

pca = PCA(n_components=2)
pc = pca.fit_transform(X_scaled)
pca.explained_variance_ratio_
print(sum(pca.explained_variance_ratio_))

pc_df = pd.DataFrame(data=pc, columns=['p1','p2'])
pc_df.index = dd.index

################################################################
# dd.plot(figsize=(20,20))

traces = []
for i, col in enumerate(dd.columns):
    # col = 'ch01_vol'
    # i = 1
    pdata = make_pdata_undup(dd, col, part=True)
    pdata = pdata.sort_index()
    traces.append(
        go.Scatter(
            x=pdata.index,
            y=pdata[col],
            mode='lines',
            # marker=dict(size=0.2),
            # select color based on index using modulus operator
            line=dict(color=COLOR_SCALE10[i % len(COLOR_SCALE10)])

        )
    )
data = traces
layout = go.Layout(template="plotly_white", title="")
fig = go.Figure(data, layout)
fig.show()
