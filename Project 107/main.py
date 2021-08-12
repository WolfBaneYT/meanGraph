import csv
import pandas as pd
import numpy as np
import plotly.graph_objects as go
df=pd.read_csv('data.csv')
print(df.groupby("level")["attempt"].mean())
fig = go.Figure(go.Bar(
    x = ['Level 1','Level 2','Level 3','Level 4'],
    y = df.groupby('level')['attempt'].mean(),
    orientation = 'v'
))
fig.show()