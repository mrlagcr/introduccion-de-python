caja1 = 23
caja2 = 50
 
Caja_resultado = caja1 - caja2
print ("resta: ", Caja_resultado)
Caja_resultado = caja1 + caja2
print ("suma: ", Caja_resultado)
Caja_resultado = caja1 / caja2
print ("division: ", Caja_resultado)
Caja_resultado = caja1 * caja2
print ("multiplicacion: ", Caja_resultado)

tupla_frutas = ("manzana", "pera", "limon")



lista_frutas = ["manzana", "pera", "limon"]


diccionario_frutas = {
    0:"manzana",
    1:"pera",
    "fruta2":"limon"


}

#ocupa dato nuemro 3 de la tupla
#print (tupla_frutas [3]) 
#respuesta fue: IndexError: tuple index out of range
#(lo pase a comentario sino se me sobre escribe y me tira error)
#pero le pido que me tire 2
print (tupla_frutas [2])
#respuesta fue: limon
#las tuplas no se pueden modificar son un dato estatico, en memoria jamas va a cambiar
#las listas si se pueden modificar o agregar mas datos de la siguiente forma
lista_frutas.append(34)
print (lista_frutas)
#respuesta fue: ['manzana', 'pera', 'limon', 34]
#como optener un dato de las listas
#lista_frutas[4]
#respuesta fue:IndexError: list index out of range
#pero si le doy uno dentro del rango pasa esto
print(lista_frutas[1])
# la solicitud de datos se cuenta asi:
#   0         1        2    siempre inicia de cero
#"manzana", "pera", "limon"
lista_cosas = ["manzana", 667.9, "limon", 56]
type(lista_cosas[1])
print(type(lista_cosas[1]))

type (diccionario_frutas)
print (type(diccionario_frutas))

#como trabajan los diccionarios
#print(diccionario_frutas.keys())
#print(diccionario_frutas.values())

"""
imprimio
dict_keys([0, 1, 'fruta2'])
dict_values(['manzana', 'pera', 'limon'])
"""
#print(diccionario_frutas.get(1))
#este comando imprime lo que hay en el valor del diccionario 1:

varCadena = "EstoEsPython3710"
variIdentificador = varCadena[6] + varCadena [12] + varCadena [13] + varCadena [14] + varCadena [15]
print (varCadena [6])
print(variIdentificador)
variIdentificador = varCadena[6] + varCadena [12] + varCadena [13:]
print(variIdentificador)
 





