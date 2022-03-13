import pandas as pd

df = pd.read_json ('https://data.nasa.gov/resource/gh4g-9sfh.json',encoding='utf8')
df = df.iloc[: , 2:]

df["geolocation"] = df['reclat'].astype(str) + ',' + df['reclong'].astype(str)

df["year"] = df["year"].str.replace("-01-01T00:00:00.000","")

print(df.head())
df.to_csv ('json_exported.csv', index = None,encoding='utf8',sep=';')
print('DataFrame is written to csv File successfully')