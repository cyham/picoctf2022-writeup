# basic-mod1

### Description

We found this weird message being passed around on the servers, we think we have a working decryption scheme. 

Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore. 

Wrap your decrypted message in the picoCTF flag format (i.e. picoCTF{decrypted_message})

### Resources

message.txt

### Solution

The text file contained a series of numbers separated by spaces. I wrote a python script, called [convertnums.py](./convertnums.py), that took each number, applied mod 37 and looked for the corresponding number in an alphabet. 

The result needed to be put inside the picoCTF{} wrapper which was then accepted as the flag. 