# Nice Netcat...

## Table of Matters

[Solution](#Solution)

[Resources](#Resources)

## Details

- **Points:** 15

- **Source:** picoCTF

- **Author:** SYREAL

## Description

There is a nice program that you can talk to by using this command in a shell: `$ nc mercury.picoctf.net 7449`, but it doesn't speak English...

### Hint 1

You can practice using netcat with this picoGym problem: [what's a netcat?](https://play.picoctf.org/practice/challenge/34)

### Hint 2

You can practice reading and writing ASCII with this picoGym problem: [Let's Warm Up](https://play.picoctf.org/practice/challenge/22)

## Solution

- Let's start by establishing a connection with the arguments given in the description with the command:

```
$ nc mercury.picoctf.net 7449
```

We get back the following output:

```
112
105
99
111
67
...
10
```

- From the second hint given to us by the challenge, I'm suspecting that the output might be a series of ASCII characters. My assumption might not be wrong seeing as each line represents a number in the range of 0 to 255.

- Let's test our theory by converting those characters from ASCII to Raw Text Format using any conversion tool you want.

We got the flag !

## Resources

- [What's a Net Cat? Solution](../whats-a-net-cat?/)
- [Let's Warm Up Solution](../lets-warm-up/)
