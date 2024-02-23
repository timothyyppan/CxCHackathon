
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