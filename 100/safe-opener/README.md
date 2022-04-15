# safe-opener

### Description

Can you open this safe? 

I forgot the key to my safe but this program is supposed to help me with retrieving the lost key.

Can you help me unlock my safe? 

Put the password you recover into the picoCTF flag format like: picoCTF{password}

### Resources

SafeOpener.java

### Solution

Step 1: Open java file in text editor

Step 2: Find the base64 encoded key

```java
    public static boolean openSafe(String password) {
        String encodedkey = "RkxBR1RJTUU";
        
        if (password.equals(encodedkey)) {
            System.out.println("Sesame open");
            return true;
        }
        else {
            System.out.println("Password is incorrect\n");
            return false;
        }
    }
```

Step 3: Decode string - I used [base64decode](https://www.base64decode.org/)

Step 4: Wrap it up in picoCTF{}

Flagtime :tada: :tada: 