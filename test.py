import pandas as pd
from datetime import datetime
import ImpactScore as imsc
import FilterFireCause as ffc
import RegionMainCauses as rmc
import numpy as np
import FireNumberTrimmer as fnt

excel_file = 'fp-historical-wildfire-data-2006-2021.xlsx'

df = pd.read_excel(excel_file, engine='openpyxl')

#df['impact_score'] = df.apply(imsc.get_impact_score(df), axis=1)

#df['fire_cause'] = df.apply(fc.filter_fire_causes, axis=1)
fire_causes = ffc.filter_fire_causes(df)

# Trimming the fire number to just the region code
df['fire_number'] = fnt.trim_fire_number(df['fire_number'])

# Test for getting a specific region's main causes
df_region_main_causes = rmc.region_main_causes(fire_causes, 'calgary')
print(df_region_main_causes)

