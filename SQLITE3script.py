# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 05:42:27 2021

@author: robin
isolation_level
Get or set the current default isolation level. None for autocommit mode or one of “DEFERRED”, “IMMEDIATE” or “EXCLUSIVE”. See section Controlling Transactions for a more detailed explanation.

in_transaction
True if a transaction is active (there are uncommitted changes), False otherwise. Read-only attribute.

New in version 3.2.

cursor(factory=Cursor)
The cursor method accepts a single optional parameter factory. If supplied, this must be a callable returning an instance of Cursor or its subclasses.

commit()
This method commits the current transaction. If you don’t call this method, anything you did since the last call to commit() is not visible from other database connections. If you wonder why you don’t see the data you’ve written to the database, please check you didn’t forget to call this method.

rollback()
This method rolls back any changes to the database since the last call to commit().

close()
This closes the database connection. Note that this does not automatically call commit(). If you just close your database connection without calling commit() first, your changes will be lost!

execute(sql[, parameters])
This is a nonstandard shortcut that creates a cursor object by calling the cursor() method, calls the cursor’s execute() method with the parameters given, and returns the cursor.

executemany(sql[, parameters])
This is a nonstandard shortcut that creates a cursor object by calling the cursor() method, calls the cursor’s executemany() method with the parameters given, and returns the cursor.

executescript(sql_script)
This is a nonstandard shortcut that creates a cursor object by calling the cursor() method, calls the cursor’s executescript() method with the given sql_script, and returns the cursor.

create_function(name, num_params, func, *, deterministic=False)
Creates a user-defined function that you can later use from within SQL statements under the function name name. num_params is the number of parameters the function accepts (if num_params is -1, the function may take any number of arguments), and func is a Python callable that is called as the SQL function. If deterministic is true, the created function is marked as deterministic, which allows SQLite to perform additional optimizations. This flag is supported by SQLite 3.8.3 or higher, NotSupportedError will be raised if used with older versions.
"""

import sqlite3
conn = sqlite3.connect(INSERT DB NAME)
cur = conn.cursor()
cur.execute(SQL Query)
cur.commit
