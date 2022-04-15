# eavesdrop

### Description

Download the packet capture and find the flag.

### Resources

capture.flag.pcap

### Solution

Step 1: Open file in wireshark

Step 2: Notice the conversation about a password and a file being transferred

Step 3: Use binwalk

```console
sam@ubuntu:~$ binwalk capture.flag.pcap

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             Libpcap capture file, little-endian, version 2.4, Ethernet, snaplen: 262144
5882          0x16FA          OpenSSL encryption, salted, salt: 0x673E2C9761096D9C
```

Step 4: Extract the file

Step 5: Under folder the encrypted file is 16FA

Step 6: Renaming the file to file.des3

Step 7: Then trying the following to decrypt (Found in chat conversation)

```console
sam@ubuntu:~$ openssl des3 -d -salt -in file.des3 -out file.txt -k flagtimepassword
```

Step 8: Open file.txt

FFFLAGTIMEEE