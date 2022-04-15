# unpackme-py

### Description

Can you get the flag? 

Reverse engineer this Python program.

### Resources

unpack.flag.py

### Solution

Step 1: Open up the python file

Step 2: Notice that there is a payload that is decoded and then executed

Step 3: Change the code so that it prints out the plain text

```python
key_str = 'correctstaplecorrectstaplecorrec'
key_base64 = base64.b64encode(key_str.encode())
f = Fernet(key_base64)
plain = f.decrypt(payload)
print(plain)
#exec(plain.decode())
```

Step 4: FLAGTIME
