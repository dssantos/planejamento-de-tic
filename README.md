# PATIC

Plano de Aquisição de TIC

[![Build Status](https://travis-ci.org/dssantos/planejamento-de-tic.svg?branch=master)](https://travis-ci.org/dssantos/planejamento-de-tic)
[![Coverage Status](https://coveralls.io/repos/github/dssantos/planejamento-de-tic/badge.svg?branch=master)](https://coveralls.io/github/dssantos/planejamento-de-tic?branch=master)

## Para desenvolver

1. Clone o repositório
2. Crie um virtualenv com python 3.7
3. Ative o virtualenv
4. Instale as dependências
5. Configure a instância com o .env
6. Execute os testes
7. Execute o servidor e abra a aplicação no endereço http://17.0.0.1:8080

### Script Unix:
```console
git clone https://github.com/dssantos/planejamento-de-tic.git patic
cd patic
python -m venv .patic
source .patic/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
manage runserver 0.0.0.0:8080
```

### Script Windows:
```console
git clone https://github.com/dssantos/planejamento-de-tic.git patic
cd patic
python -m venv .patic
.patic\Scripts\activate
pip install -r requirements.txt
copy contrib\env-sample .env
python manage.py test
manage runserver 0.0.0.0:8080
```
