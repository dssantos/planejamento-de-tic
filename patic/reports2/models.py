import pandas as pd
from django.db import models
from decouple import config

from patic.core.models import filepath


def dadospa():
    xl = pd.ExcelFile(filepath('Execução'))
    df = xl.parse("Execução")
    df = df.dropna(subset=['Unnamed: 1'])
    df = df.drop(df.index[0])
    df = df.reset_index(drop=True)
    return df
