from auxfunc import gen_pub, get_pri, encrypt, decrypt
    
#given both private and public key, encrypt and decrypt a message

original_message = raw_input('Write a message to be encrypted: ')

#set up two prime numbers
print('You will have to give two prime numbers to enrypt your message. If they are too large, it will take a long time.')
p1 = input('p1 = ')
p2 = input('p2 = ')

#generate public key - then t = (p-1)*(q-1)
n = p1*p2
tot = (p1-1)*(p2-1)

public = gen_pub(tot)
private = get_pri(public,tot)

print('Public key pair: (public,n) = (' + str(public) + ',' + str(n) + ')')
print('Private key pair: (private,n) = (' + str(private) + ',' + str(n) + ') \n')

encryp = encrypt(original_message,public,n)
decryp = decrypt(encryp,private,n)

print('Original message: ' + original_message)
print('Encrypted message: ' + str(encryp))
print('Decrypted message: ' + decryp)
