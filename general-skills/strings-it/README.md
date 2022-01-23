# strings it

## Table of Matters

[Solution](#Solution)

[Resources](#Resources)

[Notes](#Notes)

## Details

- **Points:** 100

- **Source:** picoCTF

- **Author:** SANJAY C/DANNY TUNITIS

## Description

Can you find the flag in file without running it?

### Hint 1

[strings](https://linux.die.net/man/1/strings)

## Solution

- Download the file by entering in your terminal window:

```
$ wget https://jupiter.challenges.picoctf.org/static/5bd86036f013ac3b9c958499adf3e2e2/strings
```

- As the hint indicates, we will use the `strings` command to read the content of the binary file:

```
$ strings strings
```

- There seems to be a lot of garbage in the file. We need to be able to search through all this data for our flag. In order to do so, we need to first dump the output into a text file:

```
$ strings -n 9 strings > flag.txt
```

The `-n` option is to specify the minimum length of the string.

The `>` is used to redirect stdout to overwrite a file.

- Now that all the data potentially containing our flag is saved to `flag.txt`, we can go ahead and look for our string with the command `grep`:

```
$ cat flag.txt | grep "picoCTF"
```

## Resources

- [strings Command](https://linux.die.net/man/1/strings)

## Notes

- Read your command manuals with `man [command]`.
