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
    divider = '|'
    separator_list = []
    for i in range(50):
        separator = separator_s[random.randrange(0, len(separator_s))]
        separator += separator_s[random.randrange(0, len(separator_s))]
        separator = shuffle(separator)
        separator_list.append(separator)
    return separator_list, divider.join(separator_list)

separator_list, separators = build_separators()
# print(separators)

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

p = int(input('Digite o primeiro número primo: '))
q = int(input('Digite o segundo número primo: '))

n, e, d = build_keys(p, q)
print('n => ' + str(n))
print('e => ' + str(e))
print('d => ' + str(d))

message = 'The information security is of significant importance to ensure the privacy of communications'
print('Mensagem => ' + str(message))

encrypted_message_list = []
for m in message:
    # print('encrypting \'%s\'' %m)
    m_encrypted = str(encrypt(m, n, e))
    # print('encrypted \'%s\'' %m_encrypted)
    encrypted_message_list.append(m_encrypted)

print(encrypted_message_list)
encrypted_message = encrypted_message_list[0]
for i in range(1, len(encrypted_message_list)):
    encrypted_message += separator_list[random.randrange(0, 50)] + encrypted_message_list[i]
# encrypted_message = separator_list[random.randrange(0, 50)].join(encrypted_message_list)

decrypted_message_list = re.split(separators, encrypted_message)
print(decrypted_message_list)
# print('decrypted_message_list => ' + ''.join(decrypted_message_list))

decrypted_message = ''
for c in decrypted_message_list:
    # print('decrypting \'%s\'' %c)
    m_decrypted = decrypt(int(c), n, d)
    # print('decrypted \'%s\'' %m_decrypted)
    decrypted_message += m_decrypted

print('Mensagem criptografada => ' + str(encrypted_message))
print('Mensagem descriptografada => ' + ''.join(decrypted_message))

# checar se os números são primos!
# 127
# 149