import pandas as pd 
import csv 

df = pd.read_csv("merged_star_data.csv")
del df["Luminosity"]
del df["Unnamed: 0"]

print(df.shape)
print(list(df))

df.to_csv("cleaned_star_data.csv")