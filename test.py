import pandas as pd
from datetime import datetime
import ImpactScore as imsc
import FilterFireCause as ffc
import RegionMainCauses as rmc
import numpy as np
import FireNumberTrimmer as fnt
import GetVulnerableRegions as vr

excel_file = 'fp-historical-wildfire-data-2006-2021.xlsx'

df = pd.read_excel(excel_file, engine='openpyxl')


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

df_vulnerable_regions = vr.get_vulnerable_regions(df)
print(df_vulnerable_regions)