import NormalizedCurrentSize as ncs
import DetectionTime as dt
import SpreadRate as sr
import ContainmentHectares as ch
def get_impact_score(df):
    length = len(df)
    impact_score_array = []
    for i in range(length):
        current_size = df.iloc[i]['current_size']
        impact_score = ncs.get_normalized_current_size(df, current_size)
        
        impact_score_array.append(impact_score)
    
    return impact_score_array
