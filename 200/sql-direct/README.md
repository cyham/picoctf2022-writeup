# sql-direct

### Description

Connect to this PostgreSQL server and find the flag!

### Resources

Instance

### Solution

Step 1: Start up the instance

Step 2: Connect to the psql server

```console
sam@ubuntu:~$ psql -h saturn.picoctf.net -p 51616 -U postgres
```

Step 3: Use the password

Step 4: Download and install postgresql

```console
sam@ubuntu:~$ sudo apt install postgresql-client-12
```

Step 5: Use \dt to show the table names

Step 6: Then use SELECT * FROM FLAGS;

And flagtime :smiley:
