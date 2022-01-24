# plumbing

## Table of Matters

[Solution](#Solution)

[Resources](#Resources)

[Notes](#Notes)

## Details

- **Points:** 200

- **Source:** picoCTF

- **Author:** ALEX FULTON/DANNY TUNITIS

## Description

Sometimes you need to handle process data outside of a file. Can you find a way to keep the output from this program and search for the flag? Connect to `jupiter.challenges.picoctf.org 7480`.

### Hint 1

Remember the flag format is picoCTF{XXXX}

### Hint 2

What's a pipe? No not that kind of pipe... This [kind](http://www.linfo.org/pipes.html)

## Solution

- Let's connect to `jupiter.challenges.picoctf.org 7480` with `nc`:

```
$ nc jupiter.challenges.picoctf.org 7480
```

- Seems like we won't be able to read the flag this way, We need to dump the output into a text file first using pipes as the hint suggests:

```
$ nc jupiter.challenges.picoctf.org 7480 > flag.txt
```

The `>` is used to redirect stdout to overwrite a file. Check resources to learn more about linux pipes.

- Now that all the data potentially containing our flag is saved to `flag.txt`, we can go ahead and look for our string with the command `grep`:

```
$ cat flag.txt | grep "picoCTF"
```

## Resources

- [Pipes: A Brief Introduction](http://www.linfo.org/pipes.html)

## Notes

- Read your command manuals with `man [command]`.
