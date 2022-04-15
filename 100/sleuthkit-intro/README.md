# sleuthkit-intro

### Description

Download the disk image and use mmls on it to find the size of the Linux partition. 

Connect to the remote checker service to check your answer and get the flag. 

### Resources

nc saturn.picoctf.net 52279
disk.img.gz

### Solution

Step 1: Extract disk.img

Step 2: Download and install sleuthkit

Step 3: Run mmls

```console
sam@ubuntu:~$ mmls -B disk.img
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Size    Description
000:  Meta      0000000000   0000000000   0000000001   0512B   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   1024K   Unallocated
002:  000:000   0000002048   0000204799   0000202752   0099M   Linux (0x83)
```

Step 4: Connect to saturn.picoctf.net 

Step 5: Use the length of the second partition

And you should have your flagtime