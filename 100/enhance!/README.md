# enhance!

### Description

Download the image file and find the flag.

### Resources

drawing.flag.svg - Picture of a white circle within a black circle

### Solution

Step 1: Push image through strings into its own txt file

```console
sam@ubuntu:~$ strings drawing.flag.svg > svg-strings.txt
```

Step 2: Scroll to bottom

![tspan-flag](./tspan-flag.png)

Step 3: Notice the flag in amongst each tspan section