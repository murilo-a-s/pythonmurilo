numeros = [1,2,3,4,5,6,7,8,9,10]

letras = ['a','b','c','d','e','f','h','i','j']

num = int(input("digite seu número: "))

let = str(input("digite sua letra: "))

let = let.lower()

if num in numeros and let in letras:
    print("sua entrada é válida")
else:
    print("sua entrada não é válida")

