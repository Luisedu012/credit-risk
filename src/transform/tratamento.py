import pandas as pd
import re


file_path = "data/raw_data/dados_financeiros_agricultores.csv"

df = pd.read_csv(file_path, sep=';', dtype=str)

padrao_lambda= re.compile(r'<function.*?>')
df = df[~df.apply(lambda row: row.astype(str).str.contains(padrao_lambda).any(), axis=1)]

print(df)