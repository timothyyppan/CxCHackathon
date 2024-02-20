
def filter_fire_causes(df):
   # Removing fires with undetermined causes
   df = df[df['general_cause_desc'] != 'Undetermined']
   
   # Isolating cause industry & replacing cause industries listed as "Other Industry" with their specific industries
   df.loc[df['general_cause_desc'] == 'Other Industry', \
                           'general_cause_desc'] = df.loc[df['general_cause_desc'] == 'Other Industry', 'industry_identifier_desc']
   cause_category = df['general_cause_desc']

   # Isolating activity classes and filtering out empty values
   cause_activity = df['activity_class'].dropna()

   # Isolating true cause and filtering out empty values
   true_cause = df['true_cause'].dropna()

   return cause_category, cause_activity, true_cause, df
