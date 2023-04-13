# get the order of a character
def order(chr: str) -> int:
    if len(chr) != 1:
        raise ValueError("order() expects a single character")
    if not chr.isalnum():
        return 36
    if chr.isdecimal():
        return int(chr)
    return ord(chr.lower()) - 87

# get character given the order


def rorder(order: int) -> str:
    if order == 36:
        return ' '
    if order < 10:
        return str(order)
    return chr(order + 87)


# encrypt a submessage using RSA
def encrypt_submessage(message: str, e: int, n: int) -> int:
    hashed_value = 0
    for i in range(5):
        character_order = order(message[i] if len(message) > i else ' ')
        hashed_value += character_order * (37 ** i)
    encrypted_message = pow(hashed_value, e, n)
    return encrypted_message


def encrypt(message: str, e: int, n: int) -> str:
    encrypted_message = ""
    for i in range(0, len(message), 5):
        submessage = message[i:i+5] if len(message) > i + 5 else message[i:]
        encrypted_submessage = encrypt_submessage(submessage, e, n)
        encrypted_message += str(encrypted_submessage) + " "
    return encrypted_message[:-1]


# decrypt a submessage using RSA
def decrypt_submessage(message: str, d: int, n: int) -> str:
    decrypted_value = pow(message, d, n)
    decrypted_message = ""
    for _ in range(5):
        decrypted_message = rorder(decrypted_value % 37) + decrypted_message
        decrypted_value //= 37
    return decrypted_message[::-1]


def decrypt(message: str, d: int, n: int) -> str:
    decrypted_message = ""
    for submessage in message.split():
        decrypted_submessage = decrypt_submessage(int(submessage), d, n)
        decrypted_message += decrypted_submessage
    return decrypted_message

def generate_public_and_private_key(p:int, q:int,e:int) -> tuple:
    n = p * q
    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)
    return (e, n), (d, n)

