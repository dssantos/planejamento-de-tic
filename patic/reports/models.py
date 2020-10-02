import os
import pandas as pd

from patic.core.models import filepath
from django.db import models


def dadospa():
    xl = pd.ExcelFile(filepath('Ação'))
    df = xl.parse("Planejamento")
    df = df.drop(columns=['Unnamed: 9', 'Unnamed: 10'])
    df = df.iloc[6:]
    df = df.dropna(subset=['Unnamed: 1'])
    df = df.drop(df.index[0])
    df = df.reset_index(drop=True)
    return df
