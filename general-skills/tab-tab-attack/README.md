# Tab, Tab, Attack

## Table of Matters

[Solution](#Solution)

[Resources](#Resources)

## Details

- **Points:** 20

- **Source:** picoCTF

- **Author:** SYREAL

## Description

Using tabcomplete in the Terminal will add years to your life, esp. when dealing with long rambling directory structures and filenames: `Addadshashanammu.zip`

### Hint 1

After `unzip`ing, this problem can be solved with 11 button-presses...(mostly Tab)...

## Solution

- Download the files with the command `wget`:

```
$ wget https://mercury.picoctf.net/static/72712e82413e78cc8aa8d553ffea42b0/Addadshashanammu.zip
```

- Let's unzip the file with `$ unzip Addadshashanammu.zip` as the hint suggests.

- After probing a bit with the result folder, you'll feel like there's no end to the these sub-folders. The hint indicates that this problem can be solved with 11 button-presses. What might it be?

- All you have to do is write `$ cd ` in your shell and keep pressing tab until you get to the last sub-folder.

- To get the flag, you only have to execute the file you find in your current path with the command:

```
$ ./fang-of-haynekhtnamet
```

- To go back to your home directory you just have to type:

```
$ cd ~
```

## Resources

- [cd Command](https://www.geeksforgeeks.org/cd-command-in-linux-with-examples/)
