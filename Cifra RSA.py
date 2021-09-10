import re
import random

message = 'The information security is of significant importance to ensure the privacy of communications'

def shuffle(text):
    val = random.randint(0, 1)
    if val == 0:
        return text
    elif val == 1:
        return text[::-1]

def build_separators():
    separator_s = 'abcdefghijklmnopqrstuvwxyz'
    divider = '|'
    separator_list = []
    for i in range(50):
        separator = separator_s[random.randrange(0, len(separator_s))]
        separator += separator_s[random.randrange(0, len(separator_s))]
        separator = shuffle(separator)
        separator_list.append(separator)
    return separator_list, divider.join(separator_list)

def is_coprime(num1, num2):
    # print('checking if ' + str(num1) + ' and ' + str(num2) + ' are coprimes')
    num1_dividers = []
    num2_dividers = []
    for num in range(2, num1 + 1):
        if (num1 % num == 0):
            num1_dividers.append(num)
    for num in range(2, num2 + 1):
        if (num2 % num == 0):
            num2_dividers.append(num)
    # print(str(num1) + ' => ' + str(num1_dividers))
    # print(str(num2) + ' => ' + str(num2_dividers))
    if any(num in num1_dividers for num in num2_dividers):
        # print('not coprime')
        return False
    else:
        # print('coprime')
        return True

def find_d(phi_n, e):
    d = 2
    while True:
        if ((d * e) % phi_n) == 1:
            return d
        d += 1

def build_keys(p, q):
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = 2
    while e < phi_n:
        if (is_coprime(e, phi_n)):
            break
        else:
            e += 1
    if e == phi_n:
        raise Exception('Não foi encontrado um valor \'e\' coprimo com \'phi(n)\'!')
    d = find_d(phi_n, e)
    return n, e, d

def encrypt(m, n, e):
    unicode_message = str(ord(m))
    # print('unicode_message => ' + unicode_message)
    encrypted_message = int(unicode_message) ** e % n
    return encrypted_message

def decrypt(c, n, d):
    decrypted_message = str(c ** d % n)
    # print('unicode_message => ' + decrypted_message)
    message = chr(int(decrypted_message))
    return message

def is_prime(num):
    is_prime = True
    limit = int(num * 0.1)
    if num % 2 != 0:
        for i in range(3, limit + 1, 2):
            if num % i == 0:
                return False
    else:
        return False
    if is_prime:
        return True
    else:
        return False

def try_parse_int(val):
    try:
        int(val)
        return True
    except:
        return False

separator_list, separators = build_separators()
# print(separators)

p = input('Digite o primeiro número primo: ')
q = input('Digite o segundo número primo: ')

while len(p) == 0 or len(q) == 0 or len(p) < 3 or len(q) < 3 or not try_parse_int(p) or not try_parse_int(q) or not is_prime(int(p)) or not is_prime(int(q)):
    if len(p) < 3 or len(q) < 3:
        print('Os números devem conter 3 dígitos ou mais!')
    elif len(p) == 0 or len(q) == 0 or not try_parse_int(p) or not try_parse_int(q) or not is_prime(int(p)) or not is_prime(int(q)):
        print('Um dos valores não é primo! Digite novamente...')
    p = input('Digite o primeiro número primo: ')
    q = input('Digite o segundo número primo: ')

n, e, d = build_keys(int(p), int(q))

print()
print('n => ' + str(n))
print('e => ' + str(e))
print('d => ' + str(d))
print()
print('Mensagem:\n' + str(message))
print()

encrypted_message_list = []
for m in message:
    # print('encrypting \'%s\'' %m)
    m_encrypted = str(encrypt(m, n, e))
    # print('encrypted \'%s\'' %m_encrypted)
    encrypted_message_list.append(m_encrypted)

# print(encrypted_message_list)
encrypted_message = encrypted_message_list[0]
for i in range(1, len(encrypted_message_list)):
    encrypted_message += separator_list[random.randrange(0, 50)] + encrypted_message_list[i]

decrypted_message_list = re.split(separators, encrypted_message)
# print(decrypted_message_list)

decrypted_message = ''
for c in decrypted_message_list:
    # print('decrypting \'%s\'' %c)
    m_decrypted = decrypt(int(c), n, d)
    # print('decrypted \'%s\'' %m_decrypted)
    decrypted_message += m_decrypted

print('Mensagem criptografada (com separadores):\n' + str(encrypted_message))
print()
print('Mensagem descriptografada:\n' + decrypted_message)

# é permitido apenas números primos acima de 3 dígitos
# números primos de 100 a 2000 são os mais recomendados por não necessitarem de muito processamento
# e não comprometerem a integridade dos dados