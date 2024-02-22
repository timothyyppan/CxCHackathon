#Replaces all NaN values of a column with median value
import pandas as pd
def clean_data(df, columns):   
    df = df.dropna(subset=columns)
    return df

