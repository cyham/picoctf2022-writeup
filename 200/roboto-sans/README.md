# roboto-sans

### Description

The flag is somewhere on this web application not necessarily on the website. Find it.

### Resources

Website url

### Solution

Step 1: Go to website

Step 2: Go to url/robots.txt

```html
User-agent *
Disallow: /cgi-bin/
Think you have seen your flag or want to keep looking.

ZmxhZzEudHh0;anMvbXlmaW
anMvbXlmaWxlLnR4dA==
svssshjweuiwl;oiho.bsvdaslejg
Disallow: /wp-admin/
```

Step 3: Decode base64 encoded strings

```console
sam@ubuntu:~$ echo 'ZmxhZzEudHh0' | base64 --decode
flag1.txt;
sam@ubuntu:~$ echo 'anMvbXlmaW' | base64 --decode
js/myfibase64: invalid input
sam@ubuntu:~$ echo 'anMvbXlmaWxlLnR4dA==' | base64 --decode
js/myfile.txt
sam@ubuntu:~$ echo 'svssshjweuiwl' | base64 --decode
<something...>base64 invalid input
```

Step 4: Go back to the website

Step 5: Try js/myfile.txt in the url

Flagtime :tada: :tada: