import pandas as pd
from datetime import datetime
import ImpactScore as imsc
import FireCause as fc

excel_file = 'fp-historical-wildfire-data-2006-2021.xlsx'

df = pd.read_excel(excel_file, engine='openpyxl')

#df['impact_score'] = df.apply(imsc.get_impact_score(df), axis=1)

df['fire_cause'] = df.apply(fc.get_fire_cause, axis=1)