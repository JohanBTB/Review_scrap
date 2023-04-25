# -*- coding: utf-8 -*-
import pandas as pd



def top_movies_by_genre(df, genres = [], num=3):
    for genre in genres:
        df_selected = df[df.loc[:,genre]==1]
        df_selected = df_selected.sort_values(by="score", ascending = False)
        print(f"TOP {num} {genre} MOVIES".center(60,'-'))
        for n in range(num):
            try:
                print(f"\t {n+1}.- {df_selected.iloc[n,0]}")
            except IndexError:
                print("")
                continue
        print("")
        

def segmenting_dates(x):
    movies_date = list(pd.date_range('1940-01-01', '2030-01-01',freq='5Y'))
    for i, date in enumerate(movies_date):
        if x<date:
            return movies_date[i-1]
    
