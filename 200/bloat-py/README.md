# bloat-py

### Description

Can you get the flag? 

Run this Python program in the same directory as this encrypted flag.

### Resources

- bloat.flag.py
- flag.txt.enc

### Solution

Step 1: Run bloat.flag.py in the same folder as flag.txt.enc

```console
sam@ubuntu:~$ python3 bloat.flag.py 
Please enter correct password for flag: pass
That password is incorrect
```

Step 2: Open the python file in an editor

Step 3: Notice the arg133 function

```python
def arg133(arg432):
  if arg432 == a[71]+a[64]+a[79]+a[79]+a[88]+a[66]+a[71]+a[64]+a[77]+a[66]+a[68]:
    return True
```

Step 4: Print out the 'a[71]...a[68]' to see the password

Step 5: Use the password in the program

Flagtime :fireworks: