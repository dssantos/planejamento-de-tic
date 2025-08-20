
import re, os
import locale
from decouple import config


def moeda(v):
    value = clearnumber(v)
    fvalue = "{:,.2f}".format(value)
    return fvalue if fvalue[-3] == ',' else fvalue.translate(fvalue.maketrans(',.','.,'))

def clearnumber(n):
    # Remove caracteres indesejados
    n = re.sub(r'[^0-9.].', '', str(n))
    return float(n)

def filepath(report_type):
    if report_type == 'Ação':
        file_path = config('PASTA_ACAO', default=r".\contrib\plan")
    if report_type == 'Execução':
        file_path = config('PASTA_EXEC', default=r".\contrib\exec")
    if report_type == 'Excepcionalidade':
        file_path = config('PASTA_EXCEP', default=r".\contrib\excep")

    files = []

    for r, d, f in os.walk(file_path):
        for file in f:
            if ('.xlsx' in file) and ('~$' not in file):
                files.append(os.path.join(r, file))

    return files[0]
