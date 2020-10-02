import pandas as pd
from django.db import models
from decouple import config

from patic.core.models import filepath


def dadospa():
    xl = pd.ExcelFile(filepath('Execução'))
    df = xl.parse("Execução")
    df = df.drop(columns=['Unnamed: 16', 'Unnamed: 17', 'Unnamed: 18', 'Unnamed: 19', 'Unnamed: 20', 'Unnamed: 21', 'Unnamed: 22'])
    df = df.iloc[6:]
    df = df.dropna(subset=['Unnamed: 2'])
    df = df.drop(df.index[0])
    df = df.reset_index(drop=True)
    return df
