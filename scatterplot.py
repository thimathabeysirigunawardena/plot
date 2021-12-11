import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")
fig = px.scatter(df, x="Population", y="cases",
	          size="number",color="Country",
                   size_max=60)
fig.show()
