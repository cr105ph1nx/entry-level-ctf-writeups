from Crypto.Util.number import *
import binascii

n = 1584586296183412107468474423529992275940096154074798537916936609523894209759157543
e = 65537
c = 240986837130071017759137533082982207147971245672412893755780400885108149004760496
# p, q were obtained by factorizing the 'n' on http://factordb.com/.
p = 1593021310640923782355996681284584012117
q = 521911930824021492581321351826927897005221
# calculating d with the values of e and phi
d = inverse(e, (p-1)*(q-1))
flag = pow(c, d, n)
# converting flag to raw text format
flag = binascii.unhexlify(hex(plain)[2:]).decode('utf-8')
# displaying flag
print(flag)
