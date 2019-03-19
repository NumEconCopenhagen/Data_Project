#%% [markdown]
# # Data Analysis Project

#%%
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# from matplotlib_venn import venn2
import pydst # Danmarks Statistik


#%%
Dst = pydst.Dst(lang='en') # Set language to English


#%%
Dst.get_subjects() # Get overview of Statistics Denmark's subjects


#%%
Dst.get_data(table_id = 'BB1S')


#%%
Var = Dst.get_variables(table_id = 'BB1S')


#%%
Var[:]


#%%
Var['values'][4][:10]

#%% [markdown]
# 

#%%
Dst.get_data(table_id = 'BB1S', variables={'TID':['*'], 'SÆSON':['2'], 'LAND':['W1'], 'POST':['*'], 'INDUDBOP':['N']})


#%%
df = Dst.get_data(table_id = 'BB1S', variables={'Tid':['*'], 'SÆSON':['2'], 'LAND':['W1'], 'POST':['*'], 'INDUDBOP':['N']})


#%%

PI  = df.loc[df['POST'] == 'PRIMARY INCOME', :]
tid = df.loc[df['POST'] == 'PRIMARY INCOME', :]


#%%
PI['INDHOLD']


#%%
fig, ax = plt.subplots()

ax.plot(PI['TID'],PI['INDHOLD'])

plt.show()


#%%



