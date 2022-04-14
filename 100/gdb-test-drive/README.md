# gdb-test-drive

### Description

Can you get the flag? Here's the test drive instructions:

```console
$ chmod +x gdbme
$ gdb gdbme
(gdb) layout asm
(gdb) break *(main+99)
(gdb) run
(gdb) jump *(main+104)
```

### Resources

gdbme (program)

### Solution

Literally, follow the steps given in the description and you should have your flagtime. 