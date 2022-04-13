# file-run2

### Description

Another program, but this time, it seems to want some input. What happens if you try to run it on the command line with input "Hello!"?

### Resources

run (program)

### Solution

Step 1: Use chmod to change the access permissions for the file

```console
sam@ubuntu:~$ chmod +x run
```

Step 2: Run the run file

```console
sam@ubuntu:~$ ./run
Run this file with only one argument.
```

Step 3: Try running the file with an argument inline

```console
sam@ubuntu:~$ ./run hello
Won't you say 'Hello!' to me first?
```

Step 4: Literally try 'Hello!' as the argument

```console
sam@ubuntu:~$ ./run Hello!
```

:balloon: flagtime :balloon: