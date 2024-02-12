
def get_fire_cause(row):
    # Removing fires with undetermined causes
    fire_cause = row['general_cause_desc'] != 'Undetermined'
    #if fire_cause == 'Government':
       # fire_cause
        

    return fire_cause