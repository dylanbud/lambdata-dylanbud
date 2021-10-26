import pandas as pd 
import numpy as np

def null_count(df):
    '''Counts the number of null values 
    across the entire dataframe'''
    return df.isnull().sum().sum()


def list_2_series(list_2_series, df):
    '''Takes a list and dataframe then turns the list into a series 
    and adds it to the inputted dataframe as a new column'''
    return df['List'] = list_2_series

#