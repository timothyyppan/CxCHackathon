import pandas as pd
from datetime import datetime
import ImpactScore as imsc
import FilterFireCause as ffc
import RegionMainCauses as rmc
import numpy as np

excel_file = 'fp-historical-wildfire-data-2006-2021.xlsx'

df = pd.read_excel(excel_file, engine='openpyxl')

#df['impact_score'] = df.apply(imsc.get_impact_score(df), axis=1)

#df['fire_cause'] = df.apply(fc.filter_fire_causes, axis=1)
df_filtered_causes = ffc.filter_fire_causes(df)
#df_cause_industry = df_filtered_causes[0]
#df_cause_activity = df_filtered_causes[1]
#df_true_cause = df_filtered_causes[2]
#indices = list(range(1, 10, 1))
#print(df_cause_industry.iloc[indices])
#print(df_cause_activity.head(10))
#print(df_true_cause.head(10))

df_region_main_cause = rmc.region_main_causes(df_filtered_causes, 'calgary')
print(df_region_main_cause)
#print(df_filtered_causes['general_cause_desc'].iloc[indices])
#print(df_filtered_causes['activity_class'].iloc[indices])
#indices = [90, 91, 92, 93, 94, 95, 96]
#print(df_filtered_causes.iloc[indices])