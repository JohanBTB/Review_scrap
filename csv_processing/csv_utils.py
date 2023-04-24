# -*- coding: utf-8 -*-

import os
import json
import pandas as pd

csv_files = os.path.join(os.getcwd(), "csv_processing","csv_files")

def transform_to_csv(filepath, csv_file):
    
    # Transforms the JSON file to a csv file and is saved in with the name given in the parameter "csv_file"
    json_data = pd.read_json(filepath)
    name = csv_file.split('.')[0] + "_id"
    df = pd.DataFrame(json_data)
    df.index.rename(name, inplace=True)
    df.to_csv(os.path.join(csv_files, csv_file))
    print(f"{csv_file} file created...")
    

def visualize_csv(filepath="", df=pd.DataFrame(),parse_dates = []):
    
    print("#"*60)
    
    df_name = filepath.split('\\')[-1]
    print(f"Analizando la tabla {df_name}...\n\n")
    if df.empty:
        df = pd.read_csv(filepath, sep = ",",index_col = 0, parse_dates = parse_dates)
    
    print("Numero de filas: ", len(df))
    print("Numero de columnas: ", len(df.columns))
    
    print("-"*30)
    
    print("Porcentaje de datos existentes por columnas\n")
    print(df.count()/len(df) *100)
    
    print("-"*30)
    
    for column in df.columns:
        print("Valores unicos en la columna ", column, ": ", len(df[column].unique()))
    
    print("-"*30)
    print("Tabla descriptiva")
    print(df.describe(include="all"))
    
    print("-"*30)
    
    print("Tipos de datos\n")
    print(df.dtypes)
    
    # Output the mean and median of numerical columns
    numerical_columns = df.select_dtypes(include='number').columns
    print("Total de columnas numericas: ",numerical_columns)
    return df