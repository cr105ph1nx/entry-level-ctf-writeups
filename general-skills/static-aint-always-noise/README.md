# Static Ain't Always Noise

## Table of Matters

[Solution](#Solution)

[Resources](#Resources)

## Details

- **Points:** 20

- **Source:** picoCTF

- **Author:** SYREAL

## Description

Can you look at the data in this binary: `static`? This BASH `script` might help!

## Solution

- Download the files with the command `wget`:

```
$ wget https://mercury.picoctf.net/static/66932732825076cad4ba43e463dae82f/static https://mercury.picoctf.net/static/66932732825076cad4ba43e463dae82f/ltdis.sh

```

- Let's check the type of files we have with `file [file]`

- It seems like `static` is a binary file and `ltdis.sh` is a bash script.

- Reading the content of `ltdis.sh` with `cat ltdis.sh` tells us a bit about what it's supposed to do. This bash script takes a program file as an argument and dissassembles its content into text files with the `objdump` command.

- Let's turn `ltdis.sh` into an executable with :

```
$ chmod +x ltdis.sh
```

- We now have to run the executable, and since it's expecting a program file as an argument, let's pass it the file `static` with the command :

```
$ ./ltdis static
```

The result of the execution should give us two text files.

- Let's read the file `static.ltdis.strings.txt` with the command `$ cat static.ltdis.strings.txt`. Output:

```
    238 /lib64/ld-linux-x86-64.so.2
    361 libc.so.6
    36b puts
    370 __cxa_finalize
    37f __libc_start_main
    391 GLIBC_2.2.5
    39d _ITM_deregisterTMCloneTable
    3b9 __gmon_start__
    3c8 _ITM_registerTMCloneTable
    660 AWAVI
    667 AUATL
    6ba []A\A]A^A_
    6e8 Oh hai! Wait what? A flag? Yes, it's around here somewhere!
```

- Oh seems like the flag is somewhere in this file. We can find it using the command `grep`:

```
$ cat static.ltdis.strings.txt | grep picoCTF
```

## Resources

- [Bash Scripting Cheatsheets](https://devhints.io/bash)
- [Basic Operators in Shell Scripting](https://www.geeksforgeeks.org/basic-operators-in-shell-scripting/)
