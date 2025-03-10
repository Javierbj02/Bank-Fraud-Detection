import pandas as pd
from ydata_profiling import ProfileReport

df = df = pd.read_csv('data/raw_data.csv')
profile = ProfileReport(df, title='Pandas Profiling Report')

profile.to_file("analisis.html")