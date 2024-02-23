
import RegionMainCauses as rmc
import numpy as np
import FireNumberTrimmer as fnt
import GetVulnerableRegions as vr

import pandas as pd
import math
import ImpactScore as imsc
import ColumnDatesToEpochs as cde
import FilterFireCause as ffc

import DataCleaner as dc

excel_file = 'fp-historical-wildfire-data-2006-2021.xlsx'

#Opens the excel file as a dataframe using pandas
df = pd.read_excel(excel_file, engine='openpyxl')

#Removes dates that have a typo
df.drop(index=1291, inplace=True)
df.drop(index=14316, inplace=True)

<<<<<<< Updated upstream
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


# Extracting filtered cause information
fire_causes = ffc.filter_fire_causes(df)

df = fire_causes[0]
cause_category = fire_causes[1]
cause_activity = fire_causes[2]
true_cause = fire_causes[3]

# Trimming the fire number to just the region code
df['fire_number'] = fnt.trim_fire_number(df['fire_number'])


# Test for getting a specific region's main causes
df_region_main_causes = rmc.region_main_causes('calgary', df, cause_category, cause_activity, true_cause)
print(df_region_main_causes)

# Test get vulnerable regionp

df_vulnerable_regions = vr.get_vulnerable_regions(df)
print(df_vulnerable_regions)
=======
#df['fire_cause'] = df.apply(fc.filter_fire_causes, axis=1)
df_filtered = ffc.filter_fire_causes(df) 
df_causes = df_filtered[0]
df_cause_industry = df_filtered[1]
df_cause_activity = df_filtered[2]
df_true_cause = df_filtered[3]
#indices = list(range(1, 10, 1))
#print(df_cause_industry.iloc[indices])
#print(df_cause_activity.head(10))
#print(df_true_cause.head(10))

print(df_causes)
df_region_main_cause = rmc.region_main_causes(df_filtered, 'calgary')
print(df_region_main_cause)
#print(df_filtered['general_cause_desc'].iloc[indices])
#print(df_filtered['activity_class'].iloc[indices])
#indices = [90, 91, 92, 93, 94, 95, 96]
#print(df_filtered.iloc[indices])
>>>>>>> Stashed changes
