# Based

## Table of Matters

[Solution](#Solution)

[Resources](#Resources)

## Details

- **Points:** 200

- **Source:** picoCTF

- **Author:** ALEX FULTON/DANIEL TUNITIS

## Description

To get truly 1337, you must understand different data encodings, such as hexadecimal or binary. Can you get the flag from this program to prove you are on the way to becoming 1337? Connect with `nc jupiter.challenges.picoctf.org 29221`.

### Hint 1

I hear python can convert things.

### Hint 2

It might help to have multiple windows open.

## Solution

- Let's start by establishing a connection with the command:

```
$ nc jupiter.challenges.picoctf.org 29221
```

We get back the following output:

```
Let us see how data is stored
colorado
Please give the 01100011 01101111 01101100 01101111 01110010 01100001 01100100 01101111 as a word.
...
you have 45 seconds.....

Input:

```

- My first attempt was entering the string `colorado` as an input and looks like it worked. I got back a new encoded string which looks like it was encoded in octal.

```
Input:
colorado
Please give me the  143 157 155 160 165 164 145 162 as a word.
Input:

```

- You can use online tools such as cyberchef to decode the given strings. But as the hint suggests, I chose to work with python. I made a [python script](dec.py) that takes a string in octal. decodes it and prints out the result in utf-8.

```
computer
Please give me the 636f6e7461696e6572 as a word.
Input:
```

- Welp, it gave us a new decoded string... This one looks like it's in Hexadecimal. I Added a menu to choose between OCT and HEX conversions to my python script and I was good to go. Here's how it works :

```
$ python general-skills/based/dec.py

1- Octal
2- Hexadecimal

2
Decrypted string: 636f6e7461696e6572
container
```

Of course, the connection times out after 45 seconds if it gets no user input during that time so I had to reconnect every few times to test out the script.

## Resources

- [1337](https://en.wikipedia.org/wiki/Leet)
- [Python decode](https://www.geeksforgeeks.org/python-strings-decode-method/)
- [Python codecs](https://docs.python.org/3/library/codecs.html)
