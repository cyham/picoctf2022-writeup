# basic-mod1

### Description

We found this weird message being passed around on the servers, we think we have a working decryption scheme. 

Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore. 

Wrap your decrypted message in the picoCTF flag format (i.e. picoCTF{decrypted_message})

### Resources

message.txt

### Solution

The text file contained a series of numbers separated by spaces. I wrote a python script, that took each number, applied mod 37 and looked for the corresponding number in an alphabet. 

``` python
nums = [116, 122, 111, 117, 130, 119, 123, 115]
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M','N', 'O','P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_']

print("picoCTF{", end="")
for num in nums:
    print(alphabet[num%37], end="")
print("}")
```

The result needed to be put inside the picoCTF{} wrapper which was then accepted as the flag. 