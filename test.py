import pandas as pd
from datetime import datetime
import ImpactScore as imsc
import FireCause as fc
import numpy as np

excel_file = 'fp-historical-wildfire-data-2006-2021.xlsx'

df = pd.read_excel(excel_file, engine='openpyxl')

#df['impact_score'] = df.apply(imsc.get_impact_score(df), axis=1)

#df['fire_cause'] = df.apply(fc.filter_fire_causes, axis=1)
df_filtered_causes = fc.filter_fire_causes(df)
indices = list(range(90, 121, 1))
print(df_filtered_causes['general_cause_desc'].iloc[indices])
#indices = [90, 91, 92, 93, 94, 95, 96]
#print(df_filtered_causes.iloc[indices])