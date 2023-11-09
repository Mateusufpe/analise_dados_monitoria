# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 14:31:01 2023

@author: Cisco
"""

#%% Plots simples de linha com dados de chuva

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Leitura dos dados

data = pd.read_csv('recife.csv')

# Plotagem

plt.plot(data['Category'], data['1961 - 1990'], '--r', label='1961 - 1990')
plt.plot(data['Category'], data['1991 - 2020'], '-.b', label='1991 - 2020')
plt.xticks(rotation=45)
plt.legend()
plt.show()

#%% Trabalhando com dados de vento

import numpy as np
from netCDF4 import Dataset
from mpl_toolkits.basemap import Basemap

# Dados

u = Dataset('u_default.nc')
v = Dataset('v_default.nc')

# Map

map = Basemap(projection='merc', 
              lat_0=u['XLAT'][0].mean(), lon_0=u['XLONG'][0].mean(),
              llcrnrlon=u['XLONG'][0].min(), llcrnrlat=u['XLAT'][0].min(),
              urcrnrlon=u['XLONG'][0].max(), urcrnrlat=u['XLAT'][0].max(), 
              resolution='c')

parallels = np.arange(u['XLAT'][0].min(), u['XLAT'][0].max(), 5)
meridians = np.arange(u['XLONG'][0].min(), u['XLONG'][0].max(), 5)

uu = u['U10']
vv = v['V10']

u_rec = uu[:,99,98]
v_rec = vv[:,99,98]

w_rec = np.sqrt(u_rec**2 + v_rec**2)