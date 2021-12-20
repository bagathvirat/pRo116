import pandas as pd
import plotly.express as px

df = pd.read_csv('Proj116-main\Admission_Predict.csv')
toefl_score = df["TOEFL Score"].tolist()
results = df["Chance of admit"].tolist()
fig = px.scatter(df, x=toefl_score, y=results)
fig.show()

import plotly.graph_objects as go

toefl_score = df["TOEFL Score"].tolist()
results = df["Chance of admit"].tolist()
gre_score = df["GRE Score"].tolist()
colors=[]
for data in results:
    if data == 1:
        colors.append("green")
    else:
        colors.append("red")

fig = go.Figure(data=go.Scatter(
    x=toefl_score,
    y=results,
    mode="markers",
    marker=dict(color=colors)
))                                
fig.show()