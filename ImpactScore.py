import NormalizedCurrentSize as ncs

def get_impact_score(df):
    length = len(df)
    impact_score_array = []
    for i in range(length):
        current_size = df.iloc[i]['current_size']
        reported_date = df.iloc[i]['reported_date']
        fire_start_date = df.iloc[i]['fire_start_date']
        spread_rate = df.iloc[i]['spread_rate']
        ex_hectares = df.iloc[i]['ex_hectares']
        detection_time = reported_date - fire_start_date
        containment_hectares = ex_hectares / current_size
        impact_score = ncs.get_normalized_current_size(df, current_size) \
                        + detection_time + spread_rate + containment_hectares
        impact_score_array.append(impact_score)
    
    return impact_score_array
