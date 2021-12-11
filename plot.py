import pandas as pd

import plotly.express as px

df = pd.read_csv("line_chart.csv")

fig = px.line(df, x="Date", y="Number of Coivd-19 cases", color="Country", title='Number of Covid 19 cases')

fig.show()
