import ImpactScore as impsc
import DataCleaner as dc

def get_vulnerable_regions(df):
    regions = ['C', 'E', 'H', 'G', 'L', 'M', 'P', 'R', 'S', 'W']
    
    # Calculating impact score of each wildfire
    impact_scores = impsc.get_impact_score(df)

    # Using data cleaner
    df = dc.clean_data(df, 'impact_score')

    # Summing the impact scores for each region, to get an overall region impact score
    region_impacts = [sum(impact_scores[df['fire_number'] == 'C']), \
                      sum(impact_scores[df['fire_number'] == 'E']), \
                      sum(impact_scores[df['fire_number'] == 'H']), \
                      sum( impact_scores[df['fire_number'] == 'G']), \
                      sum(impact_scores[df['fire_number'] == 'L']), \
                      sum(impact_scores[df['fire_number'] == 'M']), \
                      sum(impact_scores[df['fire_number'] == 'P'])]
   






    

    return region_impacts