# -*- coding: utf-8 -*-

import os
import json
import pandas as pd

csv_files = os.path.join(os.getcwd(), "csv_processing","csv_files")

def transform_to_csv(filepath, csv_file):
    
    json_data = pd.read_json(filepath)
    df = pd.DataFrame(json_data)
    df.to_csv(os.path.join(csv_files, csv_file))
    # return df