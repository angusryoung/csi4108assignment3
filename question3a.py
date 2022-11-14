from Crypto.Util.number import *
from Crypto import Random
import Crypto
import sys
import libnum
import math
import time

# import Crypto.Util.number

# import sys



#A
# Using RSA with 1024-bit primes p and q and a public exponent e = 65537,
# encrypt the message m = 466921883457309. Use the Chinese Remainder
# Theorem to decrypt the resulting ciphertext c; how long does it take compared to
# decryption without using CRT (show your timing results if possible)?



# Random n-bit Prime (p):  43867
# Random n-bit Prime (q):  44687

p = 64553
q = 44159

p2= 45823
q2= 34583

p3= 40231
q3= 36739

e = 65537
M = 466921883457309


n=p*q
n2=p2*q2
n3=p3*q3

PHI=(p-1)*(q-1)
PHI2=(p2-1)*(q2-1)
PHI3=(p3-1)*(q3-1)

e=65537
d=Crypto.Util.number.inverse(e,PHI)
d2=Crypto.Util.number.inverse(e,PHI2)
d3=Crypto.Util.number.inverse(e,PHI3)

print(d)



PU= [e,n] # public key
PR = [d,n] # private key

def enc(ptext):
    return pow(ptext,e, n)

def dec(ctext):
    return pow(ctext,d,n)










# Driver code
def main():

    #encrypt and decrypt in parts
    completeciphernum = [0,0,0]
    completecipherstring = ""
    print("message: " + str(M))
    ctext = enc(int(str(M)[:5]))
    completecipherstring+= str(ctext)
    completeciphernum[0]= ctext
    # print("ctext: " + str(ctext))
    
    ptext = str(dec(ctext))
    # print("ptext: " + str(ptext))

    ctext = enc(int(str(M)[5:10]))
    completecipherstring+= " "+str(ctext)
    completeciphernum[1]= ctext
    # print("cipher text: " + completecipherstring)
    ptext += str(dec(ctext))
    # print("ptext: " + str(ptext))

    ctext = enc(int(str(M)[10:]))
    completecipherstring+= " "+str(ctext)
    completeciphernum[2]= ctext
    print("cipher text: " + completecipherstring)
    ptext += str(dec(ctext))
    print("ptext: " + str(ptext))

    st = time.time()
    for i in completeciphernum:
        dec(i)
    et = time.time()
    total_time = et - st
    print('Execution time:', total_time, 'milliseconds')






if __name__ == '__main__':
    main()