#!/usr/bin/env bash
set -o xtrace

function install_redis(){
	echo "[Database] Install and configure Redis..."
	wget http://download.redis.io/redis-stable.tar.gz
	tar xvzf redis-stable.tar.gz
	rm redis-stable.tar.gz
	cd redis-stable
	make
 
	cd src && sudo make install
	make test
	cd ../utils
	sudo ./install_server.sh
}

function install_pip_venvw() {
	echo "[ENV.] Install and configure pip..."
	wget https://bootstrap.pypa.io/get-pip.py
	sudo python get-pip.py
	rm get-pip.py
    
	echo "[ENV.] Install and configure virtualenvwrapper..."
	sudo pip install virtualenvwrapper
	echo "export WORKON_HOME=$HOME/.virtualenvs" > ~/.surlenv
	echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.surlenv
	source ~/.surlenv
}
 
function create_env_install_deps(){
	echo "[ENV.] Creating environment..."
	mkvirtualenv surl
	
	echo "[ENV.] Installing requirements..."
	pip install -r requirements.txt

}

function install(){
	sudo apt-get update
	sudo apt-get install -yqq python-dev tk8.5

	install_redis
	install_pip_venvw
	create_env_install_deps
	
	echo "[!] done."
}

install
