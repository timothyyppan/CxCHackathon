
def filter_fire_causes(df):
   # Removing fires with undetermined causes
   fire_cause_filtered = df[df['general_cause_desc'] != 'Undetermined']
   fire_cause_filtered = fire_cause_filtered['general_cause_desc']
   #if df['general_cause_desc'] == 'Government':
    #  fire_cause_f
   return fire_cause_filtered
