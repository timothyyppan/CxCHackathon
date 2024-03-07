#Calculated the impact score of a wildfire
#Note that impact score is a score calculated using various factors
def get_impact_score(row):
    current_size = row['current_size']
    normalized_current_size = row['normalized_current_size']
    reported_date = row['reported_date']
    fire_start_date = row['fire_start_date']
    fire_spread_rate = row['fire_spread_rate']
    ex_hectares = row['ex_hectares']

    detection_time = reported_date - fire_start_date
    containment_hectares = ex_hectares / current_size
    impact_score = abs((normalized_current_size + detection_time + fire_spread_rate + containment_hectares) / 100000)

    return impact_score
