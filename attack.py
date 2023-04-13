
from RSA import encrypt_submessage
import time


def attack(cipher_text, plain_text, n):
    for i in range(n):
        if encrypt_submessage(plain_text, i, n) == cipher_text:
            return i 



if __name__ == '__main__':
    # first 32-bit
    ## 32-bit
    n = 916272899
    cipher_text =  474248503
    plain_text = 'hello'
    # get current time
    start = time.time()
    e = attack(cipher_text, plain_text, n)
    end = time.time()
    print(f"Time taken to crack 32-bit and get that e = {e}: {end - start} seconds")

    ## 64-bit
    plain_text = 'hello'
    cipher_text = 217839095630600804
    n = 340196134436655019
    # get current time
    start = time.time()
    e = attack(cipher_text, plain_text, n)
    end = time.time()
    print(f"Time taken to crack 64-bit and e = {e}: {end - start} seconds")


    
