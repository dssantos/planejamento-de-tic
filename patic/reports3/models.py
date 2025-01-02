import pandas as pd
from django.db import models
from decouple import config

from patic.core.models import filepath


def dadospa():
    xl = pd.ExcelFile(filepath('Excepcionalidade'))
    df = xl.parse("Excepcionalidade")
    df = df.dropna(subset=['Unnamed: 1'])
    df = df.drop(df.index[0])
    df = df.reset_index(drop=True)
    return df

def file_acoes_to_df(file):
    xl = pd.ExcelFile(file)
    df = xl.parse("Excepcionalidade")
    df = df.dropna(subset=['Unnamed: 1'])
    df = df.drop(df.index[0])
    df = df.reset_index(drop=True)
    return df
