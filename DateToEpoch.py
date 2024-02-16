import pandas as pd

def dates_to_epochs(datetime_column):
    
    datetime_column = pd.to_datetime(datetime_column)
    epoch = pd.Timestamp('1970-01-01')
    datetime_column = (datetime_column - epoch) // pd.Timedelta('1s')
    
    return datetime_column