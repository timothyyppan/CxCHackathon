
def filter_fire_causes(df):
   # Removing fires with undetermined causes
   fire_cause_filtered = df[df['general_cause_desc'] != 'Undetermined']
   
   # Checking if fire cause was listed as 'Other Industry
   is_cause_other = fire_cause_filtered[fire_cause_filtered['general_cause_desc'] == 'Other Industry']
   if is_cause_other:
      fire_cause_filtered.loc[is_cause_other] = df.loc[is_cause_other, 'industry_identifier_desc']
   # Checking if fire cause was listed as 'Government', and adding
   #is_cause_gov = fire_cause_filtered == 'Government'
   #if is_cause_gov:
   #   fire_cause_filtered.loc[is_cause_gov] += df.loc[is_cause_gov, 'industry_identifier_desc']

   
   return fire_cause_filtered
