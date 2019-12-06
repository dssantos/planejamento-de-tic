# PATIC

Plano de Aquisição de TIC

[![Build Status](https://travis-ci.org/dssantos/eventex.svg?branch=master)](https://travis-ci.org/dssantos/eventex)

## Para desenvolver

1. Clone o repositório
2. Crie um virtualenv com python 3.7
3. Ative o virtualenv
4. Instale as dependências
5. Configure a instância com o .env
6. Execute os testes

### Unix:
```console
git clone https://github.com/dssantos/planejamento-de-tic.git patic
cd patic
python -m venv .patic
source .patic/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```

### Windows:
```console
git clone https://github.com/dssantos/planejamento-de-tic.git patic
cd patic
python -m venv .patic
.patic\Script\activate
pip install -r requirements.txt
copy contrib\env-sample .env
python manage.py test
```
