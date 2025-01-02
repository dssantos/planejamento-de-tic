import os
import pandas as pd

from patic.core.models import filepath
from django.db import models


def dadospa():
    xl = pd.ExcelFile(filepath('Ação'))
    df = xl.parse("Planejamento")
    df = df.iloc[6:]
    df = df.dropna(subset=['Unnamed: 2'])
    df = df.drop(df.index[0])
    df = df.reset_index(drop=True)
    return df

def file_acoes_to_df(file):
    xl = pd.ExcelFile(file)
    df = xl.parse("Planejamento")
    df = df.iloc[6:]
    df = df.dropna(subset=['Unnamed: 2'])
    df = df.drop(df.index[0])
    df = df.reset_index(drop=True)
    return df
