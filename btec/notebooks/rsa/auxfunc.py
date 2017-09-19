import random

def gcd(a,b):
    
    #greatest common divisor
    while b != 0:
        a, b = b, a % b
    return a


def gen_pub(tot):

    #An integer public such that public and tot are coprime
    public = random.randrange(1,tot)

    #Euclid's Algorithm to verify that public and tot are comprime
    g = gcd(public,tot)
    while g != 1:
        public = random.randrange(1,tot)
        g = gcd(public,tot)
        
    return public

def get_pri(public,phi):
    d,x1,x2,y1,temp = 0,0,1,1,phi

    while public > 0:
        temp1 = temp/public
        temp2 = temp - (temp1*public)
        temp = public
        public = temp2

        x = x2 - (temp1*x1)
        y = d - (temp1*y1)

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp == 1:
        return d + phi
    
def factor(n):
    
    #calculates prime factors of a public key part n
    i = 2
    factors = []
    while (i*i <= n):
        if (n % i):
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    
    return factors    

def encrypt(message,public,n):
    
    #convert message to ascii numbers
    asciimessage = [ord(letter) for letter in message]
    
    #encrypt message using public key
    encrypted_message = []
    for j in range(len(asciimessage)):
        encrypted_message.append((asciimessage[j]**public)%n)
    
    return encrypted_message

def decrypt(encrypted_message,private,n):
    
    #decrypt message using private key
    asciidecrypted_message = []
    for j in range(len(encrypted_message)):
        asciidecrypted_message.append((encrypted_message[j]**private)%n)
    
    decrypted_message = ''.join([chr(number) for number in asciidecrypted_message])
    return decrypted_message
