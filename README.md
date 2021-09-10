O programa foi feito em Python e seu controle é por teminal.

O programa começa selecionando dois números primos aleatórios para serem usados como os valores "p" e "q".
Os números variam de uma escala de 100 a 1000 para garantir a integridade da mensagem e não exigir processamento computacional excessivo nas próximas etapas.

Os valores da chave pública "n" e "e" e da chave privada "d" devem ser calculados da seguinte forma:

n = p * q

phi(n) = (p - 1) * (q - 1)

e = um valor maior que 1 e menor e coprimo com phi(n)

d * e mod phi(n) = 1 => a partir desta fórmula, deve-se encontrar um valor de d adequado!

Sobre números coprimos:
Coprimo é quando um número em que todos os seus fatores não coincidem com os fatores de outro número exceto pelo número 1.

4 é coprimo de 5, pois 4 => 1, 2, 4 | 5 => 1, 5

8 é coprimo de 9, pois 8 => 1, 2, 4, 8 | 9 => 1, 3, 9

Para cifrar, cada caractere foi convertido para seu código em unicode e feito o seguinte cálculo:

m = caractere em unicode

c = caractere em unicode cifrado

Cifrar o caractere: c = m ** e mod n

Decifrar o caractere: m = c ** d mod n

Após a cifragem, os caracteres são juntados em uma string utilizando separadores aleatórios criados pelo programa para dar uma falsa impressão de onde começa e onde termina cada caractere.
O programa utiliza esta string para decifrar. A string então é separada e cada caractere é decifrado, resultando na mensagem final:

"The information security is of significant importance to ensure the privacy of communications".
