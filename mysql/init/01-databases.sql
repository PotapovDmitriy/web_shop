
CREATE DATABASE IF NOT EXISTS `web_shop_users`;


CREATE USER 'root'@'localhost' IDENTIFIED BY 'local';
GRANT ALL ON *.* TO 'root'@'%';