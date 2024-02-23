#Finds what industry is the main reason of either a widlfire with the final burn size, or the impact score
def get_cause_of_wf_burn(df, current_size):
    df = df[df['current_size'] == current_size]
    cat = df['general_cause_desc'].str.cat()
    
    return cat

    #return cause_info
def get_cause_of_wf_impact(df, impact_score):
    df = df[df['impact_score'] == impact_score]
    cat = df['general_cause_desc'].str.cat()

    return cat