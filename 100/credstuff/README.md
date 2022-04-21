# credstuff

### Description

We found a leak of a blackmarket website's login credentials. Can you find the password of the user cultiris and successfully decrypt it? 

The first user in usernames.txt corresponds to the first password in passwords.txt. The second user corresponds to the second password, and so on.

### Resources

- leak.tar
    - usernames.txt
    - passwords.txt

### Solution

Step 1: Extract leak.tar

Step 2: Use <kbd>CTRL+f</kbd> to find 'cultiris' in the usernames.txt file

![ctrlf-usernames](./ctrlf-usernames.png)

Step 3: Use <kbd>CTRL+g</kbd> to find the line 378 in the passwords.txt file

![ctrlg-passwords](./ctrlg-passwords.png)

Note: I was using visual studio code here so keyboard shortcuts may be different elsewhere.

Step 4: Notice that the password is encrypted

Step 5: Go to [dcode caesar-cipher](https://www.dcode.fr/caesar-cipher)

Step 6: Use the decoder to bruteforce the shift value of the password

![dcode-decrypt](./dcode-decrypt.png)

Flagtime :confetti_ball: