
def filter_fire_causes(df):
   # Removing fires with undetermined causes
   cause_industry = df[df['general_cause_desc'] != 'Undetermined']
   
   # Replacing cause industries listed as "Other Industry" with their specific industries
   cause_industry.loc[cause_industry['general_cause_desc'] == 'Other Industry', \
                           'general_cause_desc'] = cause_industry.loc[cause_industry['general_cause_desc'] == 'Other Industry', 'industry_identifier_desc']
   
   # Isolating activity classes
   
   return cause_industry
