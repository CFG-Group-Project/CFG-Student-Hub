-- CHANGE 'Current-Root-Password' to Your WORKBENCH Password
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'Current-Root-Password';
FLUSH PRIVILEGES;

CREATE DATABASE cfgdatabase CHARACTER SET utf8;
