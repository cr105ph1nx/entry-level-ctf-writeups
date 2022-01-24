# Magirkarp Ground Mission

## Table of Matters

[Solution](#Solution)

[Resources](#Resources)

## Details

- **Points:** 30

- **Source:** picoCTF

- **Author:** SYREAL

## Description

Do you know how to move between directories and read files in the shell? Start the container, `ssh` to it, and then `ls` once connected to begin. Login via `ssh` as `ctf-player` with the password, `ee388b88`

### Hint 1

Finding a cheatsheet for bash would be really helpful !

## Solution

- First of all we need to start an instance by clicking on the button "Launch Instance".

- Once your instance started, you can click on the webshell button anchored on the mid-right of the page.

- You will be asked to enter a password. Enter the one given to us by the challenge in the description `ee388b88`.

- You can then enter `ls` to list the items in your current directory. We are met with two text files, `1of3.flag.txt` looks the most interesting. We can read its contents with the command `cat`:

```
$ cat 1of3.flag.txt
```

- We seem to get one part of the flag. We know it's not the full flag because it's missing a curly bracket at the end. Let's read the content of the other file with `cat`, we might find something interesting. Output:

```
Next, go to the root of all things, more succinctly `/`
```

- `instructions-to-2of3.txt` indicates that we might find the rest of the flag in the `/` directory. We can change our current path with `cd`:

```
$ cd /
```

- Again, let's list the items in our current path with `ls`. This process should be repeated until we find all parts of the flag (It's separated into 2 parts).

## Resources

- [Secure Shell Protocol](https://en.wikipedia.org/wiki/Secure_Shell)
- [ssh Command](https://www.man7.org/linux/man-pages/man1/ssh.1.html)
