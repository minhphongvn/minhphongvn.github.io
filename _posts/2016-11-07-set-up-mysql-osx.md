---
layout:            post
title:             "Set Up MySQL in OSX with Homebrew"
menutitle:         "Set Up MySQL in OSX with Homebrew"
date:              2016-11-07 23:00:00 +0000
tags:              MySQL in OSX with Homebrew
category:          OSX Maintenance
author:            am
published:         true
redirect_from:     "/2016-11-07-set-up-mysql-osx/"
language:          EN
comments:          true
---

Quick start guide going over how I set up `MySQL` on macOS Sierra

# Contents
{:.no_toc}

* This will become a table of contents (this text will be scraped).
{:toc}

# Requirements

 - [`homebrew`][1]

# Install with `homebrew`

Update `brew` and fix any pressing issues with `doctor`

    brew update
    brew doctor

then install with

    brew install mysql

and you should receive an output similar to

    We've installed your MySQL database without a root password. To secure it run:
        mysql_secure_installation
    
    To connect run:
        mysql -uroot
    
    To have launchd start mysql now and restart at login:
      brew services start mysql
    Or, if you don't want/need a background service you can just run:
      mysql.server start
    ==> Summary
    🍺  /usr/local/Cellar/mysql/5.7.16: 13,511 files, 439M

# Secure Installation

1. Start `mysql` by running
    
        brew services start mysql

2. Run the installation script
    
        mysql_secure_installation
    
3. You will be asked to set up a `setup VALIDATE PASSWORD plugin`. Enter `y` to do this.
4. Select the required password validation (Doesn't really matter if it is just you using the database)
5. Now select `y` for all the remaining options: Remove anon. users; disallow remote root logins; 
    remove `test` database; reload privileges tables.
6. Now you should receive a message of 
    
        `All done!`

If you receive the error of 

    Error: Can't connect to local MySQL server through socket '/tmp/mysql.sock' (2)

then it is likely you don't have `mysql` running. Make sure to do the first step here

# Log in
Log in to `MySQL` as `root` with

    mysql -u root -p

See the [docs][2] for creating users, databases etc. The version can be obtained by

    mysql --version

where confusingly `Distrib` refers to the documentation number

# Managing the Background Service
The command

    brew services start mysql

will start `mysql` and this service will be started at login in perpetuity. To stop the service in
perpetuity run the command

    brew services stop mysql

further examples can be found by reading the simple [docs][3]

# Python Interface

Install [`pymysql`][4] with

	pip install pymysql

and read [here][5] for the advantages over `MySQLdb`. A simple example interfacing using
the root that was set up earlier can be seen by the following example. Log in via

	mysql -u root -p

and enter the following `SQL` code to create a test `DATABASE` and `TABLE` with

<pre class="line-numbers language-sql"><code>CREATE DATABASE example_database;
USE example_database;
CREATE TABLE `users` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `email` varchar(255) COLLATE utf8_bin NOT NULL,
    `password` varchar(255) COLLATE utf8_bin NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin
AUTO_INCREMENT=1 ;</code></pre>

now the following script saved as 
[`test_pymysql.py`]({{ site.baseurl }}/media{{page.redirect_from}}/test_pymysql.py)

<pre class="line-numbers language-python"><code>import pymysql
import argparse
import getpass

class Password(argparse.Action):
    def __call__(self, parser, namespace, values, option_string):
        if values is None:
            values = getpass.getpass()
        setattr(namespace, self.dest, values)

parser = argparse.ArgumentParser()
parser.add_argument('-u', dest='user', required=True)
parser.add_argument('-p', action=Password, nargs='?',
	 dest='password', required=True)
args = parser.parse_args()

connection = pymysql.connect(host='localhost',
	user=args.user,
	password=args.password,
	db='example_database',
	charset='utf8mb4',
	cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        cursor.execute(sql, ('webmaster@python.org',))
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()</code></pre>

and run as

	python test_pymysql.py -u root -p

to give the output of

	{u'password': u'very-secret', u'id': 1}

to remove the `example_database`, log in to `mysql` and invoke

	DROP DATABASE example_database;

# References
 - [Homebrew][1]
 - [`MySQL` Reference Manuals][2]
 - [Homebrew Services][3]
 - [`pymysql` docs][4]
 - [StackOverflow: What is PyMySQL and how does it differ from MySQLdb? ...][5]
 
[1]: http://brew.sh/
[2]: http://dev.mysql.com/doc/
[3]: https://github.com/Homebrew/homebrew-services
[4]: https://pypi.org/project/PyMySQL/
[5]: http://stackoverflow.com/q/7224807/4013571