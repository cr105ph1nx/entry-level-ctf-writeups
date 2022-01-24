import sys

option = int(input('''
1- Octal
2- Hexadecimal

'''))
enc = input("Decrypted string: ")

# If user chose oct
if(option == 1):
    # split the string into an array of strings
    enc = enc.split(" ")
    for i in range(len(enc)):
        # decode each element of enc and print it consecutively on the shell with stdout
        sys.stdout.write(chr(int(enc[i], 8)))
    print("\n")  # skip line

# If user chose hex
elif(option == 2):
    # decode enc from hex to utf-8
    print(bytes.fromhex(enc).decode('utf-8'))
    print("\n")
