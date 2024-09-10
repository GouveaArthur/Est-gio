#5) Escreva um programa que inverta os caracteres de um string.

#IMPORTANTE:
#a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
#b) Evite usar funções prontas, como, por exemplo, reverse;

def inverter_string(s):
    invertida = ''
    for char in s:
        invertida = char + invertida
    return invertida

texto = "Arthur Gouvea de Souza"
texto_invertido = inverter_string(texto)
print(texto_invertido)
