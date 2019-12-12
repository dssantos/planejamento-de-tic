from django.db import models

import os
import pandas as pd

import locale

from decouple import config


def filelist():

    pasta_exec = config('PASTA_EXEC', default="patic/core/media/exec")   # Formato Unix

    files = []

    for r, d, f in os.walk(pasta_exec):
        for file in f:
            if '.xlsx' in file:
                files.append(os.path.join(r, file))

    return files


def filepath():
    return filelist()[0]


def dadospa():
    xl = pd.ExcelFile(filepath())
    df = xl.parse("Execução")
    df = df.drop(columns=['Unnamed: 0', 'Unnamed: 16', 'Unnamed: 17', 'Unnamed: 18', 'Unnamed: 19', 'Unnamed: 20', 'Unnamed: 21', 'Unnamed: 22'])
    df = df.dropna(subset=['Unnamed: 2'])
    df.columns = df.iloc[0]
    df = df.drop(df.index[0])
    df = df.reset_index(drop=True)
    return df


def moeda(v):
    valor = v
    locale.setlocale(locale.LC_ALL, '')
    valor = locale.currency(valor, grouping=True, symbol=None)
    return valor
