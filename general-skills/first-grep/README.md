# First Grep

## Table of Matters

[Solution](#Solution)

[Resources](#Resources)

[Notes](#Notes)

## Details

- **Points:** 100

- **Source:** picoCTF

- **Author:** ALEX FULTON/DANNY TUNITIS

## Description

Can you find the flag in file? This would be really tedious to look through manually, something tells me there is a better way.

### Hint 1

[grep tutorial](https://ryanstutorials.net/linuxtutorial/grep.php)

## Solution

- Download the file by entering in your terminal window:

```
$ wget https://jupiter.challenges.picoctf.org/static/5bd86036f013ac3b9c958499adf3e2e2/strings
```

- As the hint indicates, we will use the `grep` command to find our string within the file:

```
$ cat file | grep "picoCTF"
```

We pass `grep` the argument `picoCTF` since we know that that's the string our flag starts with.

## Resources

- [grep Command](https://man7.org/linux/man-pages/man1/grep.1.html)

## Notes

- Read your command manuals with `man [command]`.
