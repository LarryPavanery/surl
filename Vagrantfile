# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.hostname = "surl"

  config.vm.network "forwarded_port", guest: 80, host: 8888     # HTTP
  config.vm.network "forwarded_port", guest: 8000, host: 3000   # FALCON FRAMEWORK
  config.vm.network "forwarded_port", guest: 6379, host: 9999   # SERVICE REDIS

  config.vm.synced_folder ".", "/development"

  config.vm.provider "virtualbox" do |vb|
     vb.gui = false
     vb.name = "pydev"
     vb.cpus = 1
     vb.memory = "2048"
  end

  config.vm.provision "shell", privileged: false, inline: <<-SHELL
     sudo apt-get update
     sudo apt-get install -yqq vim git curl python-dev tk8.5

     #Install pip
     wget https://bootstrap.pypa.io/get-pip.py
     sudo python get-pip.py
     rm get-pip.py

     #Configure Virtual Env.
     sudo pip install virtualenvwrapper
     echo "export WORKON_HOME=$HOME/.virtualenvs" >> ~/.bashrc
     echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc
     source ~/.bashrc
     
     #Install Redis
     wget http://download.redis.io/redis-stable.tar.gz
     tar xvzf redis-stable.tar.gz
     cd redis-stable
     make

     cd src && sudo make install
     make test
     cd ../utils
     sudo ./install_server.sh


  SHELL
end
