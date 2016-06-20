# Aplicação
Shortened url - SURL

# Sobre
API para encurtar URLs.

A aplicação faz uso dos seguintes pacotes:
* [Falcon Framework](https://falconframework.org/) - Falcon is a very fast, very minimal Python web framework for building microservices, app backends, and higher-level frameworks.
* [Ujson](https://pypi.python.org/pypi/ujson) - UltraJSON is an ultra fast JSON encoder and decoder written in pure C with bindings for Python 2.5+ and 3.
* [Gunicorn](http://gunicorn.org/) - Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX. It's a pre-fork worker model ported from Ruby's Unicorn project. The Gunicorn server is broadly compatible with various web frameworks, simply implemented, light on server resources, and fairly speedy.
* [Eventlet](http://eventlet.net/) - Eventlet is a concurrent networking library for Python that allows you to change how you run your code, not how you write it.
* [Redis](http://redis.io/) - Redis is an open source (BSD licensed), in-memory data structure store, used as database, cache and message broker. It supports data structures such as strings, hashes, lists, sets, sorted sets with range queries, bitmaps, hyperloglogs and geospatial indexes with radius queries. Redis has built-in replication, Lua scripting, LRU eviction, transactions and different levels of on-disk persistence, and provides high availability via Redis Sentinel and automatic partitioning with Redis Cluster.

# Ambiente
A aplicação utiliza ambiente virtualizado com Virtualenvwrapper.
- Ubuntu 14.04

# Instalação

Descompacte o pacote e entre na pasta do projeto:
```sh
$ tar -vzxf surl.tar.gz
$ cd surl
```

Execute o script de instalação:
```sh
$ source install.sh
```
O processo de instalação irá realizar as seguintes configurações:

- Instalação de dependências no ambiente Ubuntu
- Instalação e configuração do banco de dados Redis
- Instalação do pip e Virtualenvwrapper
- Criação do ambiente virtual para a aplicação
- Instalação das dependências da aplicação no ambiente virtual
 
# Execução
Para iniciar a aplicação, execute o start:
```sh
$ source start.sh
```

# Testes e Cobertura
Para executar os testes, com o ambiente virtual criado, execute:
```sh
$ tox -e py27
```
> Será criado um diretório com o resultado dos testes de cobertura.

 Ou instale manualmente as dependências e execute os testes da seguinte forma:
 ```sh
$ pip install -r test-requirements.txt
$ nosetests --verbose
```
Para ter o resultado dos testes e cobertura, execute o seguinte comando:
 ```sh
$ tools/combine_coverage.sh
```
- Será criada uma pasta "coverage_html", abra o index html para verificar o resultado.
# Check style
Para verificar Lint da aplicação, estilo, execute o seguinte comando:
 ```sh
$ tox -e pep8
```
> O comando pep8 faz uso do autopep8, pacote responsável por corrigir estilos não desejados.

# =D



