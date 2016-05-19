# Install
#sudo pip install --upgrade django
# Git
#git clone https://github.com/DonAlPatino/stepic.git /home/box/web

# MySQL
echo 'innodb_use_native_aio = 0' | sudo tee --append /etc/mysql/my.cnf
sudo service mysql restart
sudo mysql -uroot -e "CREATE DATABASE ask CHARACTER SET utf8 COLLATE utf8_general_ci;"
sudo mysql -uroot -e "GRANT ALL PRIVILEGES ON ask.* TO 'ask_user'@'localhost' IDENTIFIED BY '123456789';"