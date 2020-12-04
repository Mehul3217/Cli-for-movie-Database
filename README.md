# CLI for Movie Database


## Installation Instructions
### MySQL
To install MySQL server on Ubuntu, run the following commands

```
sudo apt-get update
sudo apt-get install mysql-server
```

When installing the MySQL server for the first time, it will prompt for a root password that you can later login with. 

The start command is
```
mysql -u <user_name> -p <password>
```

If for some reason, you aren't asked for the password during installation, try prepending the start command with sudo and provide your root password. You can now set a root password or create a new user. 

To create a new user, you may use the following command
```
CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';
```
At this stage the created user doesn't have access to the data. To allow access, you'll have to run a grant access query as below
```
GRANT ALL PRIVILEGES ON * . * TO 'newuser'@'localhost';
```
```
```

### PyMySQL

PyMySQL is an interface for connection to the MySQL server from Python.

To install PyMySQL, you can use one of the two routes  
**Pip**
```
pip install PyMySQL
```
**Conda**
```
conda install -c anaconda pymysql
```
### To Run
To run the code, you will need to login with a username and password(your MYSQL username and password) which has access to the COMPANY database.

```
python3 app.py
```

This will prompt for you to enter your username and password.
