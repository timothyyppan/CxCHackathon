def get_cause_of_wf_burn(df, current_size):
    df = df[df['current_size'] == current_size]
    cat = df['general_cause_desc'].str.cat()
    act = df['activity_class'].str.cat()
    tc = df['true_cause'].str.cat()
    return cat, act, tc

    #return cause_info
def get_cause_of_wf_impact(df, impact_score):
    df = df[df['impact_score'] == impact_score]
    cat = df['general_cause_desc'].str.cat()
    act = df['activity_class'].str.cat()
    tc = df['true_cause'].str.cat()
    return cat, act, tc