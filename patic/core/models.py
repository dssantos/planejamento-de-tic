
import re, os
import locale
from decouple import config


def moeda(v):
    valor = clearnumber(v)
    locale.setlocale(locale.LC_ALL, '')
    valor = locale.currency(valor, grouping=True, symbol=None)
    return valor

def clearnumber(n):
    # Remove caracteres indesejados
    n = re.sub('[^0-9\.].', '', str(n))
    return float(n)

def filepath(report_type):
    if report_type == 'Ação':
        file_path = config('PASTA_ACAO', default=".\contrib\plan")   # Formato Unix
    if report_type == 'Execução':
        file_path = config('PASTA_EXEC', default=".\contrib\exec")   # Formato Unix

    files = []

    for r, d, f in os.walk(file_path):
        for file in f:
            if ('.xlsx' in file) and ('~$' not in file):
                files.append(os.path.join(r, file))

    return files[0]
