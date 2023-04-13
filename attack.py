
from RSA import encrypt_submessage, generate_public_and_private_key
import time


def attack(cipher_text, plain_text, n):
    for i in range(n):
        if encrypt_submessage(plain_text, i, n) == cipher_text:
            return i 



if __name__ == '__main__':
    plain_text = 'hello'
    for bits in range(30,40):
        public_key, private_key = generate_public_and_private_key(bits)
        cipher_text = encrypt_submessage(plain_text,private_key[0],private_key[1])
        start = time.time()
        attack(cipher_text,plain_text,public_key[1])
        end = time.time()
        print(f'it take {end - start} seconds to attack with {bits} bits')




    
