# PATIC

Plano de Aquisição de TIC

[![Build Status](https://travis-ci.org/dssantos/planejamento-de-tic.svg?branch=master)](https://travis-ci.org/dssantos/planejamento-de-tic)
[![Coverage Status](https://coveralls.io/repos/github/dssantos/planejamento-de-tic/badge.svg?branch=master)](https://coveralls.io/github/dssantos/planejamento-de-tic?branch=master)
[![Maintainability](https://api.codeclimate.com/v1/badges/d37f8f1beb8822511efb/maintainability)](https://codeclimate.com/github/dssantos/planejamento-de-tic/maintainability)

## Para desenvolver

1. Clone o repositório
2. Crie um virtualenv com python 3.7
3. Ative o virtualenv
4. Instale as dependências
5. Defina as variáveis no arquivo .env

6. Execute os testes
7. Execute o servidor e abra a aplicação no endereço http://127.0.0.1:8080

### Script Unix:
```console
git clone https://github.com/dssantos/planejamento-de-tic.git patic
cd patic
python -m venv .patic
source .patic/bin/activate
pip install -U pip
pip install -r requirements.txt
cp contrib/env-sample .env
cat .env

python manage.py test
python manage.py runserver 0.0.0.0:8080
```

### Script Windows:
```console
git clone https://github.com/dssantos/planejamento-de-tic.git patic
cd patic
python -m venv .patic
.patic\Scripts\activate
pip install -U pip
pip install -r requirements.txt
copy contrib\env-sample .env
type .env

python manage.py test
python manage.py runserver 0.0.0.0:8080
```

### Script Windows (Git Bash com comandos Linux):
```console
git clone https://github.com/dssantos/planejamento-de-tic.git patic
cd patic
python -m venv .patic
source .patic/Scripts/activate
pip install -U pip
pip install -r requirements.txt
cp contrib/env-sample .env
cat .env

python manage.py test
python manage.py runserver 0.0.0.0:8080
```