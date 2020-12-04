# CS4.301-Data-and-Applications-Project-Template

This repository will serve as a template for the aformentiontioned course project. The instructions and tools given here are compatible with python 3.X. The corresponding instructions and tools for python 2 have already been provided in the course moodle page.


## Administrivia

Your projects will be evaluated on **13th November** during the lab session (8:30 - 11:30). You will demonstrate all the features of your projects and will be graded by the TAs.

This has already been announced in the lab.


## Installation Instructions

I trust that the students reading this are all at a respectable age to be able to handle installation bugs themselves and won't be needing the TAs to help them. 

### MySQL

Although you haven't strictly been told to explicitly use MySQL it is highly recommended. To install MySQL server on Ubuntu, run the following commands

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

Here, I would also like to point out that if your application involves a login or some form of authentication, you may do so using the USER table of the MYSQL database that exists by default. 

To create a new user, you may use the following command
```
CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';
```
At this stage the created user doesn't have access to the data. To allow access, you'll have to run a grant access query as below
```
GRANT ALL PRIVILEGES ON * . * TO 'newuser'@'localhost';
```

It is also possible to grant a new user access to only one database or some tables of a database. If your application involves different user types with different access clearences, you may use this feature.

With this you must be in a place to be able to play around with MySQL. Since this template has been made to work on top of the COMPANY dataset, proceed to load the dataset using the following command within the mysql environment
```
source path_to_COMPANY.sql;
```

### PyMySQL

Again although you weren't explicitly told to use PyMySQL it is recommended that you do.

That being said, **YOU CANNOT USE PANDAS OR OTHER PYTHON LIBRARIES TO DO THIS PROJECT**

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

## Boilerplate

We have provided a boilerplate piece of code just to get you started (althought I hope you already have). Similar code snippets in Python2 have already been provided. The only reason this bioler plate is being shared is to show you what an acceptable UI looks like.  
### To Run
To run the boilerplate code, you will need to login with a username and password(your MYSQL username and password) which has access to the COMPANY database.

```
python3 boilerPlate.py
```

This will prompt for you to enter your username and password.

### UI Interface
Due to the timeline, you are not expected to implement a graphical UI (although you aren't disallowed either). A CLI (Command Line Interface) will do for the sake of the project

You can also have different interfaces depending on which kind of user logged in to your software. Under the assumption that someone from adminstration logged into mine, the UI for the boilerplate looks something like this
```
1. Hire a new employee
2. Fire an employee
3. Promote an employee
4. Employee Statistics
5. Logout

Enter Choice > 
```

Only one function has been implemented in the code provided. But it's enough to give you an idea about what you have to do.

### Error Handling

Although in this code, error handling hasn't explicitly been handled, you have to handle errors appropriately.  

For example, if you try to delete a department, you can only do so after you've reassigned all the employess to another department. Or if you want to fire the manager of a department, you can only do so after assigning the department a new manager (where again, yes, the manager has to satisfy the foreign key constrain i.e. should be an employee himself)

Instead of handling all the errors yourself, you can make use of error messages which MySQL returns. You might find this useful to implement when you want to debug as well
```
try:
    do_stuff()
except Exception as e:
    print (e)
```
resource: https://stackoverflow.com/questions/25026244/how-to-get-the-mysql-type-of-error-with-pymysql

## Miscellaneous 

For those of you who want to implement a messaging option, you can make a simple abstract of it by implementing a table like below. You are not expected to make a real time version due to the time contraints even if you have added said function to your requirements.

```
CREATE TABLE MESSAGES( 
    Essn1 CHAR(9) NOT NULL, 
    Essn2 CHAR(9) NOT NULL, 
    Timestamp TIMESTAMP NOT NULL, 
    Message VARCHAR(1000), 
    PRIMARY KEY(Essn1, Essn2, Timestamp), 
    FOREIGN KEY (Essn1) REFERENCES EMPLOYEE(Ssn)
    FOREIGN KEY(Essn2) REFERENCES EMPLOYEE(Ssn) );
    
```

## Resources

* https://www.python.org/dev/peps/pep-0249/
* https://dev.mysql.com/doc/connector-python/en/
* http://zetcode.com/python/pymysql/
* https://www.tutorialspoint.com/python3/python_database_access.htm
* https://o7planning.org/en/11463/connecting-mysql-database-in-python-using-pymysql
* https://www.journaldev.com/15539/python-mysql-example-tutorial

