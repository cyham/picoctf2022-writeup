nums = [116, 122, 111, 117, 130, 119, 123, 115]
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M','N', 'O','P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_']

print("picoCTF{", end="")
for num in nums:
    print(alphabet[num%37], end="")
print("}")