# Wave A Flag

## Table of Matters

[Solution](#Solution)

[Resources](#Resources)

[Notes](#Notes)

## Details

- **Points:** 10

- **Source:** picoCTF

- **Author:** SYREAL

## Description

Can you invoke help flags for a tool or binary? This program has extraordinarily helpful information...

### Hint 1

This program will only work in the webshell or another Linux computer.

### Hint 2

To get the file accessible in your shell, enter the following in the Terminal prompt:

`$ wget https://mercury.picoctf.net/static/beec4f433e5ee5bfcd71bba8d5863faf/warm`

### Hint 3

Run this program by entering the following in the Terminal prompt: `$ ./warm`, but you'll first have to make it executable with `$ chmod +x warm`

### Hint 4

-h and --help are the most common arguments to give to programs to get more information from them!

### Hint 5

Not every program implements help features like -h and --help.

## Solution

- Download the file provided by the challenge using `wget` like so:

```
$ wget https://mercury.picoctf.net/static/beec4f433e5ee5bfcd71bba8d5863faf/warm
```

- We run the command `file [file]` to check the type of file we're dealing with. We are prompted with the response:

```
$ warm: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=506b7be935d8940c672ab0d40d2e03ebd746155b, with debug_info, not stripped
```

The first line indicating that it's an executable file.

- Let's try and execute this file shall we? But first, we need to turn it into an executable with the command:

```
$ chmod +x warm
```

- Once that done, let's execute it by running:

```
$ ./warm
```

We get the following response: `Hello user! Pass me a -h to learn what I can do!`

- Let's pass the executable the `-h` option just like we do with the commond commands that you know:

```
$ ./warm -h
```

Look at that, now we got the flag !

## Resources

- [ELF Binaries in Linux](https://linux-audit.com/elf-binaries-on-linux-understanding-and-analysis/)
- [Permissions in Linux](https://www.geeksforgeeks.org/permissions-in-linux/)
- [Command-Line Options](http://www.catb.org/~esr/writings/taoup/html/ch10s05.html)

## Notes

- Remember to make reading the manual of the commands you use a habit. `man [cmd]` is your friend!
