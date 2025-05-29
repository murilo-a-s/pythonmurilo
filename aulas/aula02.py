import math

#int
#string
#float
#list
#bulian

# criar uma func que faça soma
# func divisao
# func multiplicação
# func q escreva frase
# func recebe 5 arg e faz a media e retorne frase falando "media tal"
# usar print


def soma(arg1, arg2):
    soma = arg1 + arg2
    return soma

def multi(arg1, arg2):
    multi = arg1 * arg2
    return multi

def divi(arg1, arg2):
    divi = arg1 / arg2
    return divi

def frase(arg):
    print(arg)

def media(arg1, arg2, arg3, arg4, arg5):
    soma = arg1 + arg2 + arg3 + arg4 + arg5
    media = soma / 5
    print("a media das suas notas é:", media)

media(8,9,7,10,5)
    

   
