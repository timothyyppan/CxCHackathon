import pandas as pd
import math
import ImpactScore as imsc
import ColumnDatesToEpochs as cde
import FilterFireCause as ffc
import ModelTrainer as mt
import ModelUse as mu
import DataCleaner as dc

excel_file = 'fp-historical-wildfire-data-2006-2021.xlsx'

#Opens the excel file as a dataframe using pandas
df = pd.read_excel(excel_file, engine='openpyxl')

#Removes dates that have a typo
df.drop(index=1291, inplace=True)
df.drop(index=14316, inplace=True)

#Calculates the magnitude of the current_size column
magnitude_all_current_sizes= math.sqrt((df['current_size']**2).sum())

#Creates a column and fills it with the normalized current_size
df['normalized_current_size'] = magnitude_all_current_sizes / df['current_size']

#Converts all date/time to epoch
cde.column_dates_to_epochs(df)

#Creates a column and fills it with the calculated impact score
df['impact_score'] = df.apply(imsc.get_impact_score, axis=1)

#Removes any rows that are bad
columns_with_nans = ['fire_spread_rate', 'temperature', 'relative_humidity', 'wind_speed', 'ex_hectares', 'impact_score']
df = dc.clean_data(df, columns_with_nans)

#Trains the model **Need to optimize the model**
model = mt.train_model(df)

print(df['impact_score'])


#For tomorrow, implement a linear regression model
#and see if it is better than the tensor
#Also try and improve the tensor model (try multiplying the predictions to manually get the right value)
stop = False
while(stop == False):
    stop_input = input("Stop? ")
    if stop_input == 'Yes':
        stop == True
    current_size = input("current_size: ")
    assessment_hectares = input("assessment_hectares: ")
    fire_spread_rate = input("fire_spread_rate: ")
    temperature = input("temperature: ")
    relative_humidity = input("relative_hymidity: ")
    wind_speed = input("wind_speed: ")
    uc_hectares = input("uc_hectares: ")

    new_features = pd.DataFrame({
        'current_size': [current_size],
        'assessment_hectares': [assessment_hectares],
        'fire_spread_rate': [fire_spread_rate],
        'temperature': [temperature],
        'relative_humidity': [relative_humidity],
        'wind_speed': [wind_speed],
        'uc_hectares': [uc_hectares]
        })
    mu.use_model(model, new_features)
#df['fire_cause'] = df.apply(ffc.filter_fire_causes, axis=1)
#df_filtered_causes = ffc.filter_fire_causes(df)
#print(df_filtered_causes.iloc[12])