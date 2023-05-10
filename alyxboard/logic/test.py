import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

def rleid(aserise):
    # aserise = df[col]
    char = "sixx"
    group = 0
    result = []
    for i in aserise.index: #range(0, len(aserise)):
        # i = 11
        if aserise[i] == char:
            result.append(group)
        else:
            group = group + 1
            result.append(group)
            char = aserise[i]
    return result



def make_pdata_undup(df, col):
    uniqueIdx = ~(pd.Series(rleid(df[col])).duplicated(keep='first')) | \
                ~(pd.Series(rleid(df[col])).duplicated(keep='last')) 
    pdata = df.loc[ uniqueIdx.tolist()]           
    return pdata

# dd = px.data.stocks()
# dd.iloc[:, 1:] = dd.iloc[:, 1:].apply(lambda x: round(x, 2))

# df = dd.set_index('date')
# #sum(df.duplicated(subset=['GOOG']))

# pdata = make_pdata_undup(df, 'GOOG')

# trace1 = go.Scatter(
#     x=pdata.index, y=pdata['GOOG'], 
#     mode='markers', marker=dict(size=3))
# layout = go.Layout()
# fig = go.Figure([trace1], layout)
# fig.show()




dd = px.data.stocks()
dd.iloc[:, 1:] = dd.iloc[:, 1:].apply(lambda x: round(x, 2))
dd = dd.loc[11:30]
dd.iloc[4,2] = 0.96

df = dd.set_index('date')

# df.reset_index()
#sum(df.duplicated(subset=['GOOG']))

pdata = make_pdata_undup(dd, 'AAPL')

trace1 = go.Scatter(
    x=pdata.index, y=pdata['AAPL'], 
    mode='markers+lines', marker=dict(size=13))
layout = go.Layout()
fig = go.Figure([trace1], layout)
fig.show()



dd = pd.DataFrame({'grp':["a","a","a","c","c","b","b","b","b"]})
dd['gid'] = rleid(dd['grp'])

dd = pd.DataFrame({'grp':["a","a","a","c","c","b","b","b","b"]})
dd_filtered = dd[1:] # DataFrame에서 슬라이스 사본에 값을 설정하려고 할 때 
dd_filtered['gid'] = rleid(dd_filtered['grp'])
# pandas에서 DataFrame을 슬라이스하면 복사본이 아닌 원본 DataFrame의 보기가 반환됩니다. 
# 즉, 슬라이스에 대한 모든 변경 사항은 원본 DataFrame에도 영향을 미칩니다. 
# 그러나 경우에 따라 Pandas는 보기 또는 복사본으로 작업하는지 여부를 결정할 수 없으므로 경고를 발행하여 알려줍니다.
# 
# 이 경고를 피하고 원래 DataFrame을 수정하고 있는지 확인하려면 
# 슬라이스에 값을 직접 설정하는 대신 .loc[row_indexer, col_indexer] = value를 사용해야 합니다. 
# .loc은 레이블 기반 인덱싱을 통해 DataFrame의 값에 액세스하고 수정할 수 있는 방법이며,
#  이를 사용하여 원본 DataFrame을 수정하고 있음을 pandas에 명시적으로 알립니다.


다음은 .loc을 사용하여 DataFrame의 값을 수정하는 방법의 예입니다.

import pandas as pd

# create a sample data frame
dfo = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]})
# modify a value using .loc
dfo.loc[1, 'Age'] = 31
print(dfo)

df = pd.DataFrame([
    [ 1,  2,  3,  4,  5],
    [ 6,  7,  8,  9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
], index = ['ridx1', 'ridx2', 'ridx3', 'ridx4'],
   columns=['colNm1', 'colNm2', 'colNm3', 'colNm4', 'colNm5'])

df.loc[['ridx1','ridx2'], ]
df.iloc[0,:]
df.iloc[[0,1,2]]
df.iloc[range(0,2)]

df.iloc[1]
df.iloc[[1]]
df.loc['ridx1']
df['colNm1']  



df.iloc[:, range(0,2l)]
df.loc[['ridf.loc[df['colNm1']>6]

df.loc[[False, False, True, True]]
df.loc[[False, False, True, True], :]

df.iloc[[False, False, True, True]]
df.iloc[[False, False, True, True], :]

df.loc[ df['colNm1'].isin([11,16]), : ]


df.loc[ (df['colNm1'].isin([6,11,16])) & (df['colNm4']>10), : ]


exam.reset_index(drop=False, inplace=True)
exam.set_index(["class", "name"], inplace =True)
exam


ex_df = pd.DataFrame(
    np.arange(0, 9).reshape(3, 3),
    index=['i0', 'i1', 'i2'],
    columns=['col0', 'col2', 'col3']
)


ex_df.reset_index(drop=False)
ex_df.set_index(["col0","col3"], inplace=True)

ex_df.index
#                 col2
# col0	col3
# 0	    2	    1
# 3	    5	    4
# 6	    8	    7

ex_df.reset_index(drop=True,  inplace=False)
ex_df.reset_index()
