# file-types

### Description

This file was found among some files marked confidential but my pdf reader cannot read it, maybe yours can.

### Resources

Flag.pdf

### Solution

:exclamation: DANGER STRUGGLES AHEAD :exclamation:

Step 1: Push file through strings to see what I can find

```console
sam@ubuntu:~$ strings Flag.pdf > flag-pdf-strings.txt
```

SEE: What looks like a shell script 

![strings-sh](./strings-sh.png)

Step 2: Right click on file and rename fo Flag.sh

Step 3: Change the permissions of the file to allow it to run

```console
sam@ubuntu:~$ chmod +x Flag.sh 
```

Step 4: Run the file

```console
sam@ubuntu:~$ ./Flag.sh
x - created lock directory _sh00046.
x - extracting flag (text)
./Flag.sh: 119: uudecode: not found
restore of flag failed
flag: MD5 check failed
x - removed lock directory _sh00046.
```
But this didn't run the .sh file correctly... so...

Step 5: Search > what is uudecode?

- uudecode is associated with the sharutils package

Step 6: Download and install sharutils

```console
sam@ubuntu:~$ sudo apt install sharutils
```

Step  7: Rerun the file

```console
sam@ubuntu:~$ ./Flag.sh
x - created lock directory _sh00046.
x - extracting flag (text)
x - removed lock directory _sh00046.
```
Success!!

Step 8: cat the flag file that is created

![cat-flag](./cat-flag.png)

SEE: Illegable text BUT notice !`<arch>` at the top of the file

Step 9: Search > what is !`<arch>`?

- ar (Unix) > https://en.wikipedia.org/wiki/Ar_(Unix)
- https://linux.die.net/man/1/ar

Step 10: Extract the file from the archive

```console
sam@ubuntu:~$ ar x flag
```

SEE: Another archive...

Step 11: Put file in [checkfiletype](https://www.checkfiletype.com/)

- Discover file is a cpio file

Extra: (I rename the file from flag to archive.cpio)

Step 12: Extract cpio archive

```console
sam@ubuntu:~$ cpio -iv < archive.cpio
```

SEE: Another archive...

Step 13: Put file in [checkfiletype](https://www.checkfiletype.com/)

- Discover file is a bzip2 file

Step 14: Extract bzip2 archive

```console
sam@ubuntu:~$ bzip2 -d flag
```

(This overwrote the old flag file to flag.out)

SEE: Another archive...

Step 15: Put file in [checkfiletype](https://www.checkfiletype.com/)

- Discover file is a gzip file

Step 16: Extract gzip file 

(I had to rename the original file to something other than flag)

DO: GUI folder > Double click > Extract

SEE: Another archive... 

Step 17: Put file in [checkfiletype](https://www.checkfiletype.com/)

- Discover file is a lzip file

Step 18: Download and install lzip

```console
sam@ubuntu:~$ sudo apt install lzip
```

Step 19: Extract lzip file

```console
sam@ubuntu:~$ lzip -d flag
```

SEE: Another archive... (flag.out file)

Step 20: Put file in [checkfiletype](https://www.checkfiletype.com/)

- Discover file is a lz4 file

Step 21: Extract lz4 file

```console
sam@ubuntu:~$ lz4 -d flag.out flag
```

SEE: Another archive...

Step 22: Put file in [checkfiletype](https://www.checkfiletype.com/)

- Discover file is a lzma file

Step 23: Extract lzma file

```console
sam@ubuntu:~$ lzma -d flag.xz
```

SEE: Another archive...

Step 24: Put file in [checkfiletype](https://www.checkfiletype.com/)

- Discover file is a lzop file

Step 25: Download and install lzop

```console
sam@ubuntu:~$ sudo apt install lzop
```

Step 26: Change file suffix to .lzo 

Step 27: Extract lzop file

```console
sam@ubuntu:~$ lzop -d current.lzo > current
```

SEE: Another archive...

Step 28: Extract lzip file

```console
sam@ubuntu:~$ lzip -d current > current.out
```

NOTE: Everything under here may have flaws in as my notes became less frequent

Step 29: Download and install p7zip

```console
sam@ubuntu:~$ sudo apt install p7zip
```

SEE: Another archive...

Step 31: Extract p7zip file

```console
sam@ubuntu:~$ p7zip -d current.out > current
```

Step 32:

```console
sam@ubuntu:~$ cat current
706963Gf4354467b464c414754494d457d
```

Step 33: Put text in [rapidtables](https://www.rapidtables.com/convert/number/hex-to-ascii.html)

FLAGTIME :balloon: :balloon: :balloon:

![](https://giphy.com/gifs/planeteclipse-run-flag-l0HU1Ajixx0bg86oU)
