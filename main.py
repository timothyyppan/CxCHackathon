import pandas as pd
import math
import ImpactScore as imsc
import ColumnDatesToEpochs as cde
import FilterFireCause as ffc
import ModelTrainer as mt

excel_file = 'fp-historical-wildfire-data-2006-2021.xlsx'

#Opens the excel file as a dataframe using pandas
df = pd.read_excel(excel_file, engine='openpyxl')

#Removes any rows that are bad (Typos)
df.drop(index=1291, inplace=True)
df.drop(index=14316, inplace=True)
#Should probably remove any entries that don't have a fire_start_date or we should replace it with the average detection time or smthn

#Calculates the magnitude of the current_size column
magnitude_all_current_sizes= math.sqrt((df['current_size']**2).sum())

#Creates a column and fills it with the normalized current_size
df['normalized_current_size'] = magnitude_all_current_sizes / df['current_size']

#Converts all date/time to epoch
cde.column_dates_to_epochs(df)

#Creates a column and fills it with the calculated impact score
df['impact_score'] = df.apply(imsc.get_impact_score, axis=1)

mt.train_model(df)

#df['fire_cause'] = df.apply(ffc.filter_fire_causes, axis=1)
#df_filtered_causes = ffc.filter_fire_causes(df)
#print(df_filtered_causes.iloc[12])