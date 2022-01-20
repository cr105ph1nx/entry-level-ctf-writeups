# Python Wrangling

## Table of Matters

[Solution](#Solution)

[Resources](#Resources)

[Notes](#Notes)

## Details

- **Points:** 10

- **Source:** picoCTF

- **Author:** SYREAL

## Description

Python scripts are invoked kind of like programs in the Terminal... Can you run this Python script using this password to get the flag?

### Hint 1

Get the Python script accessible in your shell by entering the following command in the Terminal prompt:

`$ wget https://mercury.picoctf.net/static/5c4c0cbfbc149f3b0fc55c26f36ee707/ende.py`

### Hint 2

`$ man python`

## Solution

- Download the three files provided by the challenge using `wget` like so:

```
$ wget https://mercury.picoctf.net/static/5c4c0cbfbc149f3b0fc55c26f36ee707/ende.py

$ wget https://mercury.picoctf.net/static/5c4c0cbfbc149f3b0fc55c26f36ee707/pw.txt

$ wget https://mercury.picoctf.net/static/5c4c0cbfbc149f3b0fc55c26f36ee707/flag.txt.en
```

- As the description of the challenge states, we need to somehow run the script in `ende.py` with the password in `pw.txt` to get the flag from `flag.txt.en`. I notice that the file containing the flag ends with the extension `en` and the python script's name is `ende` which might lead me to believe that it is an "EN"-"Decryptor". My suspicion was confirmed by reading the code.

- First thing we need to try is to run the python script

```
python ende.py
```

- Once the command ran, this usage instruction appears: `Usage: ende.py (-e/-d) [file]`

- I assume the `-e` option means to encrypt the file, and `-d` to decrypt it. Again, my suspicion is confirmed by running `python ende.py -h` (-h for help), I get the following message:

```
Usage: ende.py (-e/-d) [file]
Examples:
  To decrypt a file named 'pole.txt', do: '$ python ende.py -d pole.txt'
```

- Now that we understand how the script works we only need to run the following command:

```
python ende.py -d flag,txt.en
```

- Once you get asked for the password, just copy the password given in the `pw.txt` file.

## Resources

- [Command-Line Options](http://www.catb.org/~esr/writings/taoup/html/ch10s05.html)

## Notes

- Remember to make reading the manual of the commands you use a habit. `man [cmd]` is your friend!
