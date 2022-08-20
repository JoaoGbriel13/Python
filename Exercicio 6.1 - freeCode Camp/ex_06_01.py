str = 'X-DSPAM-Confidence: 0.8475'

#Achando a posição no index da string
strFind = str.find(':')
print(strFind)

#Cortando a string a partir da posição achada com o metodo find
strSliced = str[strFind+2:]
print(strSliced)

#Transformando a string em float
strFloat = float(strSliced)
print(strFloat)

#Verificando o tipo das variaveis
print(type(strFind))
print(type(strSliced))
print(type(strFloat))