#Importamos la funcion de busqueda 
from ast import While
from tracemalloc import start
from googlesearch import search
from numpy import array;
from pyparsing import Word;
#word = str(input("dijite la palabra clave a buscar: "));

"Palabras claves a buscar"

word = ["carro + rojo","carro","colegio + cafeteria","problematica + tienda + colegio + aglomeracion"]

""" Parametros que se usan para ajilizar la busqueda mas exhautiva"""
tld = "com" #Esta bandera es el dominio
lang = "en" #Esta bandera es el lenguaje español
num = 100 #Esta bandera es el umero de links a mostrar
start = 0 #Salta los primeros 10 o 100 resultados
stop = num #Para si el valor es false la busqueda es infinita
pause = 2.0 #TIEMPO DE ESPERA DE 2.0 SEGUNDOS PARA BUSQUEDAS ESTO SI ESTA MUY LARGO GOOGLE NOS BANEA POR LA IP

for i in word:
    print(i)
    print("----------------------------------------------------------------------------------- PALABRA NUEVA CLAVE---------------------------------------------------------------------------------")
    result = search(i, tld=tld, lang=lang, num=num, start=start, stop=stop, pause=pause);
    for i in result:
        print(i)


"""
recorremos para imprimir las url
que puedan ser de nuestra utilidad 
"""

"""
for i in result:
    print(i);
    
"""