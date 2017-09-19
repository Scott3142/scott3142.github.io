from auxfunc import factor, get_pri, encrypt, decrypt
import time

#given public key, crack private key and decrypt a message
#Example: (public,n) = (17,629); encrypt = [463L, 492L, 567L, 567L, 111L]
public = input('Input first part of public key pair (public,n): public = ')
n = input('Input second part of public key pair (public,n): n = ')
encryp = input('Input encrypted message: ')

start_time = time.time()
p1,p2 = factor(n)
tot = (p1-1)*(p2-1)

crack_private = get_pri(public,tot)
decryp = decrypt(encryp,crack_private,n)
elapsed_time = time.time() - start_time

print('\nDecrypted message: ' + decryp)
print('\nTime taken to crack: ' + str(elapsed_time) + ' seconds.')    
