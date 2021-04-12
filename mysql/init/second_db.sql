# create databases
CREATE DATABASE IF NOT EXISTS `web_shop_users`;

# create root user and grant rights
CREATE USER 'root'@'localhost' IDENTIFIED BY 'local';
GRANT ALL ON *.* TO 'root'@'%';