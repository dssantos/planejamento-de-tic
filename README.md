# PATIC

Plano de Aquisição de TIC

[![Build Status](https://travis-ci.org/dssantos/planejamento-de-tic.svg?branch=master)](https://travis-ci.org/dssantos/planejamento-de-tic)

## Para desenvolver

1. Clone o repositório
2. Crie um virtualenv com python 3.7
3. Ative o virtualenv
4. Instale as dependências
5. Configure a instância com o .env
6. Execute os testes
7. Roda o servidor e abre a aplicação no navegador

### Unix:
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

### Windows:
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
