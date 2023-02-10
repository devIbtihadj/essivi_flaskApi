apt-get update
sudo apt install mysql-client
apt-get install -y libmariadb-dev-compat libmariadb-dev
sudo apt-get install -y default-libmysqlclient-dev
pip3 install --disable-pip-version-check --target . --upgrade -r requirements.txt
