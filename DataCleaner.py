#Replaces all NaN values of a column with median value
def clean_data(df, columns):   
    for column in columns:
        median_value = df[column].median()
        df.loc[:, column] = df[column].fillna(median_value)

    return df

