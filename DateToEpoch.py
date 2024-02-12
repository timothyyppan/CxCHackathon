import pandas as pd
from datetime import datetime

def datetime_to_epoch(datetime):
    if pd.isnull(datetime):
        return None
    date_format = "%Y-%m-%d %H:%M"