from ast import Lambda
from operator import truediv

# tipos basicos 
idade =27
ano =1995

print(type(idade))
print(type(ano))

nome = 'Alyce'
idade = 25
altura = 1.75
feriado = True

print(type(nome))
print(type(idade))
print(type(altura))
print(type(feriado))
print(type(feriado),(altura))

#variaveis 

velocidade_do_carro = 200
print(velocidade_do_carro)

#variaveis float

sua_altura = 1.77
print(sua_altura)

gosto_de_chocolate = True
print(gosto_de_chocolate)

#string 
frase_boas_vindas = 'Sejam bem vindas ao Luiza Code'
print(frase_boas_vindas)

#esta retornando a sua variavél no terminal não o tipo

#operadores aritimeticos

seis = 6
dez = 10

soma = seis+dez
print (soma)

subtração = seis-dez
print (subtração)

divisão = seis / dez
print (divisão)

multiplicação = seis*dez
print (multiplicação)

Divisão_interna = seis // dez
print (Divisão_interna)

modulo = seis % dez
print (modulo)

exponenciacao = seis ** dez
print (exponenciacao)

#operadores de comparação
variavel = 5

#igual a 
if variavel == 5:
    print ('os valores são iguais')
# diferente de     
if variavel != 5:
    print ('o valor da variavel não é igual a 7')   
# maior que     
if variavel > 2:
    print ('o valor da variavel é maior que 2')
#maior ou igual a    
if variavel >= 5:
    print ('o valor da variavel é maior ou igual 5')
#menor ou igual     
if variavel <= 7:
    print ('o valor da variavel é menor ou igual a 7')
#menor     
if variavel < 5:
    print ('o valor da variavel é menor que 5')   


#operadores de atribuição    

# = equivale a x=1 
# += equivale a x=x+1
# -= equivale a x=x-1
# *= equivale a x=x*1
# /= equivale a x=x/1
# %= equivale a x=x%1


# = equivale a x=1 
numero = 5

numero += 7
print(numero) #soma 5+7= 12 (atribui)

# -= equivale a x=x-1
numero = 5
    
numero -=3
print(numero)# 5-3 =2 

# *= equivale a x=x*1
numero = 5

numero*=2
print(numero)#5*2 =10

# /= equivale a x=x/1
numero = 5

numero /=4
print(numero) #5/4 

# %= equivale a x=x%1
numero = 5

numero %=2
print(numero)       
                
num1 = 7
num2 = 4

#exemplo operador and : Retorna True se ambas condições forem verdadeiras
if num1 > 3 and num2 <8:
    print('as duas condições são verdadeiras')     

# exemplo operador or : Retorna True se uma das condições forem verdadeiras
if num1 > 4 or num2 <=8:
    print(' uma ou duas condições são verdadeiras') 

#exemplo operador not   : Retorna falso se o valor for verdadeiro    
if num1 < 30 and num2 < 8 :
    print( 'inverte o resultado da condição entre os parametros')
    
#conversão de tipos 

a=15
print(f'a variavel é do tipo: {type(a)}')
b=10.6

a = a+b    # soma o inteiro com float e virou um float 
print(f'a variavel é do tipo: {type(a)}')
print(f'valor da soma:{a}')   

lista = ['luizacode']
print(type(lista))

