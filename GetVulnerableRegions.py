import ImpactScore as impsc

def get_vulnerable_regions(df):
    regions = ['C', 'E', 'H', 'G', 'L', 'M', 'P', 'R', 'S', 'W']
    
    # Calculating impact score of each wildfire
    impact_scores = impsc.get_impact_score(df)


    return impact_scores