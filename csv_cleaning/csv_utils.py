# -*- coding: utf-8 -*-

import os
import pandas as pd
import re
csv_files = os.path.join(os.getcwd(), "csv_cleaning","csv_files")

def dropping(df, drops = [],dropna = False ):
    df = df.drop(drops, axis = 1)
    if dropna:
        df.dropna(inplace = True)
    
    return df
    
def to_minutes(runtime):
    if "h" in runtime:
        hours, minutes = re.findall(r"\d+", runtime)
        return str(int(hours)*60 + int(minutes))
    else:
        minutes = runtime.replace(' min','').replace('m','')
        return minutes if minutes else ''
    