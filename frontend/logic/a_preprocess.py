import pickle
import pandas as pd
import numpy as np
import os

from alyxdash import DATA_DIRECTORY


dataPath = DATA_DIRECTORY+'/issue_02'
dataPath_pre = dataPath+'_pre'
if not os.path.exists(dataPath_pre):
    os.makedirs(dataPath_pre)
# dataPath = '/Users/onesixx/my/git/alyxdash/data/issue_02'
files = os.listdir(dataPath)

# 컬럼명
data_colNm = ['time']
data_colNm.extend([f'ch{i+1:02d}_{j}' for i in range(56)
                  for j in ['vol', 'curr', 'q', 'pv']])
data_colNm.extend([f'temp_{i+1}' for i in range(12)])


# proc = [f'proc_{i+1:02d}' for i in range(3)]
files_proc_01 = []
for file in files:
    fileNm = os.path.splitext(file)[0]
    fileExt = os.path.splitext(file)[1]
    if fileExt == '.csv':
        if '_'.join(fileNm.split("_")[:2]) == 'proc_01':
            files_proc_01.append(file)  # f'{fileNm}{fileExt}')

fch3 = {}
pch1 = {}
pch2 = {}
for file in files_proc_01:
    # file = 'proc_01_T1_3_PCH1_Equip212_P218_T71299_T76051_20221205_135524.csv'
    fileNm = os.path.splitext(file)[0]
    fileExt = os.path.splitext(file)[1]
    if fileNm.split("_")[4] == 'FCH':
        formation_data = pd.read_csv(os.path.join(
            dataPath, file), encoding='ISO-8859-1')
        formation_data.columns = data_colNm
        fch3['data'] = formation_data
        fch3['fileNm'] = fileNm
        fch3['issuecell'] = '_'.join(fileNm.split("_")[2:4])
        fch3['equip'] = fileNm.split("_")[5]
        fch3['P'] = fileNm.split("_")[6]
        fch3['tray1'] = fileNm.split("_")[7]
        fch3['tray2'] = fileNm.split("_")[8]
        fch3['date'] = fileNm.split("_")[9]
        fch3['time'] = fileNm.split("_")[10]
        with open(os.path.join(dataPath_pre, 'proc_01_fch3.pickle'), 'wb') as fw:
            pickle.dump(pch1, fw)
    if fileNm.split("_")[4] == 'PCH1':
        formation_data = pd.read_csv(os.path.join(
            dataPath, file), encoding='ISO-8859-1')
        formation_data.columns = data_colNm
        pch1['data'] = formation_data
        pch1['fileNm'] = fileNm
        pch1['issuecell'] = '_'.join(fileNm.split("_")[2:4])
        pch1['equip'] = fileNm.split("_")[5]
        pch1['P'] = fileNm.split("_")[6]
        pch1['tray1'] = fileNm.split("_")[7]
        pch1['tray2'] = fileNm.split("_")[8]
        pch1['date'] = fileNm.split("_")[9]
        pch1['time'] = fileNm.split("_")[10]
        with open(os.path.join(dataPath_pre, 'proc_01_pch1.pickle'), 'wb') as fw:
            pickle.dump(pch1, fw)
    if fileNm.split("_")[4] == 'PCH2':
        formation_data = pd.read_csv(os.path.join(
            dataPath, file), encoding='ISO-8859-1')
        formation_data.columns = data_colNm
        pch2['data'] = formation_data
        pch2['fileNm'] = fileNm
        pch2['issuecell'] = '_'.join(fileNm.split("_")[2:4])
        pch2['equip'] = fileNm.split("_")[5]
        pch2['P'] = fileNm.split("_")[6]
        pch2['tray1'] = fileNm.split("_")[7]
        pch2['tray2'] = fileNm.split("_")[8]
        pch2['date'] = fileNm.split("_")[9]
        pch2['time'] = fileNm.split("_")[10]
        with open(os.path.join(dataPath_pre,'proc_01_pch2.pickle'), 'wb') as fw:
            pickle.dump(pch2, fw)
