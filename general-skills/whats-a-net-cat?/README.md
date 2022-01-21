# What's A Net Cat?

## Table of Matters

[Solution](#Solution)

[Resources](#Resources)

[Notes](#Notes)

## Details

- **Points:** 100

- **Source:** picoCTF

- **Author:** SANJAY C/DANNY TUNITIS

## Description

Using netcat (nc) is going to be pretty important. Can you connect to `jupiter.challenges.picoctf.org` at port `64287` to get the flag?

### Hint 1

nc [tutorial](https://linux.die.net/man/1/nc)

## Solution

- The manual for netcat explains how we need to use the tool to establish a basic connection. From the synopsis, we get:

```
nc [-46DdhklnrStUuvzC] [-i interval] [-p source_port] [-s source_ip_address] [-T ToS] [-w timeout] [-X proxy_protocol] [-x proxy_address[:port]] [hostname] [port[s]]
```

- We only have two arguments, the hostname and port number. So based on the synopsis, to establish a basic connect to the `jupiter.challenges.picoctf.org` host on port `64287`, we need to run the following command:

```
nc jupiter.challenges.picoctf.org 64287
```

## Resources

- [netcat manual](https://linux.die.net/man/1/nc)

## Notes

- Remember to make reading the manual of the commands you use a habit. `man [cmd]` is your friend!

- RTFM
