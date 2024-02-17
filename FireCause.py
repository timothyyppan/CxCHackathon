
def filter_fire_causes(df):
   # Removing fires with undetermined causes
   cause_filtered = df[df['general_cause_desc'] != 'Undetermined']
   
   # Isolating cause industry & replacing cause industries listed as "Other Industry" with their specific industries
   cause_filtered.loc[cause_filtered['general_cause_desc'] == 'Other Industry', \
                           'general_cause_desc'] = cause_filtered.loc[cause_filtered['general_cause_desc'] == 'Other Industry', 'industry_identifier_desc']
   cause_industry = cause_filtered['general_cause_desc']

   # Isolating activity classes and filtering out empty values
   cause_activity = cause_filtered['activity_class'].dropna()

   # Isolating true cause and filtering out empty values
   true_cause = cause_filtered['true_cause'].dropna()

   return cause_industry, cause_activity, true_cause
