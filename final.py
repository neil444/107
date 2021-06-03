import pandas as pd
import csv
import plotly.graph_objects as go

df = pd.read_csv("c:/Users/ADI/Downloads/Data-Analysis-by-visualisation-master/Data-Analysis-by-visualisation-master/data.csv")

student_df = df.loc[df['student_id'] == "TRL_987"]
student_df1 = df.loc[df['student_id'] == "TRL_xsl"]
student_df2 = df.loc[df['student_id'] == "TRL_abc"]
student_df3 = df.loc[df['student_id'] == "TRL_xyz"]
student_df4 = df.loc[df['student_id'] == "TRL_zet"]
student_df5 = df.loc[df['student_id'] == "TRL_abc"]

print(student_df.groupby("level")["attempt"].mean())
print(student_df1.groupby("level")["attempt"].mean())
print(student_df2.groupby("level")["attempt"].mean())
print(student_df3.groupby("level")["attempt"].mean())
print(student_df4.groupby("level")["attempt"].mean())
print(student_df5.groupby("level")["attempt"].mean())


fig = go.Figure(go.Bar(
            x=student_df.groupby("level")["attempt"].mean(),
          
            y=['Level 1', 'Level 2', 'Level 3', 'Level 4'],
            orientation='h'))

fig.show()
