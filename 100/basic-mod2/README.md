# basic-mod2

### Description

A new modular challenge! 

Take each number mod 41 and find the modular inverse for the result. Then map to the following character set: 1-26 are the alphabet, 27-36 are the decimal digits, and 37 is an underscore. 

Wrap your decrypted message in the picoCTF flag format (i.e. picoCTF{decrypted_message})

### Resources

message.txt

### Solution

Similar to the basic-mod1 challenge, I reused the code from there, but performed the modular multiplicative inverse calculation on the number from the array.

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

The result needed to be put inside the picoCTF{} wrapper which was then accepted as the flag. 