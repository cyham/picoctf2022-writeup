# patchme-py

### Description

Can you get the flag? Run this Python program in the same directory as this encrypted flag.

### Resources

- patchme.flag.py
- flag.txt.enc

### Solution

Step 1: Run the patchme.flag.py

Make sure the flag.txt.enc is in the same folder

```console
sam@ubuntu:~$ python3 patchme.flag.py
Please enter correct password for flag:
```

But we do not know the password yet :disappointed:

Step 2: Open the python file in a editor 

Step 3: Notice a if statement check for 

```python
user_pw = input("Please enter correct password for flag: ")
    if( user_pw == "ak98" + \
                   "-=90" + \
                   "adfjhgj321" + \
                   "sleuth9000"):
        print("Welcome back... your flag, user:")
```

Step 4: Reconstruct the string from 'ak98' onwards

Flagtime :boom:
