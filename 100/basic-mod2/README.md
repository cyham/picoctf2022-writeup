# basic-mod2

### Description

A new modular challenge! 

Take each number mod 41 and find the modular inverse for the result. Then map to the following character set: 1-26 are the alphabet, 27-36 are the decimal digits, and 37 is an underscore. 

Wrap your decrypted message in the picoCTF flag format (i.e. picoCTF{decrypted_message})

### Resources

message.txt

### Solution

Step 1: Open message.txt in text editor

Step 2: Notice the text file contains a series of numbers separated by spaces

Step 3: Write a python script that takes each number, applies the modular multiplicative inverse, applies mod 41 and looks for the corresponding number in an alphabet

``` python
# Greatest Common Divisor
def egcd(a, b): 
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)
# Modular Multiplicative Inverse
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

nums = [294, 393, 206, 211, 203, 237, 224, 238]
alphabet = ['#','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M','N', 'O','P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_']

print("picoCTF{", end="")
for num in nums:
    print(alphabet[modinv(num,41)], end="")
print("}")
```

Step 4: Put the result inside the picoCTF{} wrapper

### References

https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm