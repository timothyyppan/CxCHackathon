#Gets the regions with the highest impact score
#Note that impact score is a score calculated using various factors
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
                      sum(impact_scores[df['fire_number'] == 'G']), \
                      sum(impact_scores[df['fire_number'] == 'L']), \
                      sum(impact_scores[df['fire_number'] == 'M']), \
                      sum(impact_scores[df['fire_number'] == 'P']), \
                      sum(impact_scores[df['fire_number'] == 'R']), \
                      sum(impact_scores[df['fire_number'] == 'S']), \
                      sum(impact_scores[df['fire_number'] == 'W'])  ]
   
    # Pairing each region with its corresponding impact score
    paired_regions_scores = list(zip(regions, region_impacts))

    # Sorting the pairs by impact score in descending order
    sorted_pairs = sorted(paired_regions_scores, key=lambda x: x[1], reverse=True)

    # Extract the sorted regions
    sorted_regions = [region for region, score in sorted_pairs]

    # Determining top 3 most vulnerable regions
    top_vulnerable_regions = [sorted_regions[0], sorted_regions[1], sorted_regions[2]]

    return top_vulnerable_regions