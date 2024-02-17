import pandas as pd
import math
import ImpactScore as imsc
import ColumnDatesToEpochs as cde
import FilterFireCause as fc

excel_file = 'fp-historical-wildfire-data-2006-2021.xlsx'

df = pd.read_excel(excel_file, engine='openpyxl')

df.drop(index=1291, inplace=True)
df.drop(index=14316, inplace=True)
#Should probably remove any entries that don't have a fire_start_date or we should replace it with the average detection time or smthn
magnitude_all_current_sizes= math.sqrt((df['current_size']**2).sum())
df['normalized_current_size'] = magnitude_all_current_sizes / df['current_size']
cde.column_dates_to_epochs(df)

df['impact_score'] = df.apply(imsc.get_impact_score, axis=1)

print(df[['impact_score']].head)

#df['fire_cause'] = df.apply(fc.filter_fire_causes, axis=1)
#df_filtered_causes = fc.filter_fire_causes(df)
#print(df_filtered_causes.iloc[12])