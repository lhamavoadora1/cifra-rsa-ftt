import re
import random

def shuffle(text):
    val = random.randint(0, 1)
    if val == 0:
        return text
    elif val == 1:
        return text[::-1]

def build_separators():
    separator_s = 'abcdefghijklmnopqrstuvwxyz'
    separator_n = '1234567890'
    divider = '|'
    separator_list = []
    for i in range(50):
        separator = separator_s[random.randrange(0, len(separator_s))]
        separator += separator_n[random.randrange(0, len(separator_n))]
        # print('separator => ' + separator)
        separator = shuffle(separator)
        # print('shuffled separator => ' + separator)
        separator_list.append(separator)
    return separator_list, divider.join(separator_list)

separator_list, separators = build_separators()
print(separators)

# coprimo é um número que todos os seus divisores não coincidem entre si exceto pelo número 1
# 4 é coprimo de 5, pois 4 => 1, 2, 4 e 5 => 1, 5
# 8 é coprimo de 9, pois 8 => 1, 2, 4, 8 e 9 => 1, 3, 9
# phi é igual a quantidade de números menores que n, coprimos com respeito a ele

# se x é primo, então phi_x = x - 1

# selecionar dois primos p e q
# fazer o cálculo n = p * q

# escolher um número inteiro e que esteja entre 1 e phi(n) que deve ser coprimo com phi(n)
# calcule d = (2 * phi(n) + 1) / e
# chave pública é composta por n e e
# chave privada é composta por d

# cifrar a mensagem c = m**e mod n
# decifrar a mensagem m = c**d mod n

def is_coprime(num1, num2):
    print('checking if ' + str(num1) + ' and ' + str(num2) + ' are coprimes')
    num1_dividers = []
    num2_dividers = []
    for num in range(2, num1 + 1):
        if (num1 % num == 0):
            num1_dividers.append(num)
    for num in range(2, num2 + 1):
        if (num2 % num == 0):
            num2_dividers.append(num)
    print(str(num1) + ' => ' + str(num1_dividers))
    print(str(num2) + ' => ' + str(num2_dividers))
    if any(num in num1_dividers for num in num2_dividers):
        print('not coprime')
        return False
    else:
        print('coprime')
        return True

# def egcd(a, b):
#     if a == 0:
#         return (b, 0, 1)
#     else:
#         g, y, x = egcd(b % a, a)
#         return (g, x - (b // a) * y, y)

# def modinv(a, m):
#     g, x, y = egcd(a, m)
#     if g != 1:
#         raise Exception('modular inverse does not exist')
#     else:
#         return x % m

def find_d(phi_n, e):
    i = 2
    while True:
        # print('result')
        # print(((i * e) % phi_n))
        if ((i * e) % phi_n) == 1:
            return i
        elif i > 9999999:
            print('reached limit!')
            break
        i += 1

def build_keys(p, q):
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = 2
    while e < phi_n:
        if (is_coprime(e, phi_n)):
            break
        else:
            e += 1
    # gcd, a, b = egcd(e, phi_n)
    d = find_d(phi_n, e)
    print('d => ' + str(d))
    return n, e, d

def encrypt(m, n, e):
    unicode_list = []
    # for letter in m:
    unicode_list.append(str(ord(m)))
    # print(unicode_list)
    unicode_message = str(ord(m))#separator_list[random.randrange(0, 50)].join(unicode_list)
    print('unicode_message => ' + str(unicode_message))
    # encrypted_message = int(unicode_message) ** e % n# wrong
    # encrypted_message = pow(int(unicode_message) ** e, -1, n)
    # gcd, a, b = egcd(int(unicode_message) ** e, n)
    encrypted_message = int(unicode_message) ** e % n
    # print('encrypted_message => ' + str(encrypted_message))
    return encrypted_message

def decrypt(c, n, d):
    # decrypted_message = str(c ** d % n)# wrong
    # decrypted_message = pow(c ** d, -1, n)
    # gcd, a, b = egcd(c ** d, n)
    # decrypted_message = str(a)
    decrypted_message = str(c ** d % n)
    # print('decrypted_message => ' + str(decrypted_message))
    # unicode_list = decrypted_message.split(divider)
    letter_list = []
    # for unicode in unicode_list:
    letter_list.append(chr(int(decrypted_message)))
    message = ''.join(letter_list)
    # print(message)
    return message

p = int(input('Digite o primeiro número primo: '))
q = int(input('Digite o segundo número primo: '))

n, e, d = build_keys(p, q)
print(n, e, d)

message = 'olá meus consagrados, tudo firmezão?!?'#'The information security is of significant importance to ensure the privacy of communications'

encrypted_message_list = []
for m in message:
    encrypted_message_list.append(str(encrypt(m, n, e)))
encrypted_message = separator_list[random.randrange(0, 50)].join(encrypted_message_list)
print('encrypted_message => ' + str(encrypted_message))

decrypted_message_list = re.split(separators, encrypted_message)
print('decrypted_message_list => ' + ''.join(decrypted_message_list))

decrypted_message = ''
for c in decrypted_message_list:
    decrypted_message += decrypt(int(c), n, d)
# decrypted_message = decrypt(int(encrypted_message), n, d)
print('decrypted_message => ' + ''.join(decrypted_message))

# checar se os números são primos!
# 127
# 149