"""
	•	En una escuela dieron las notas de 10 estudiantes, a continuación, están los 10 estudiantes:
	•	María: 70
	•	José: 55
	•	Jenny: 99
	•	Juanita: 88
	•	Pedro: 89
	•	Sofía: 100
	•	Valeria: 24
	•	Fernanda: 67
	•	Julian: 55
	•	Oscar: 99
Indicaciones:
	•	Indicar la cantidad de personas que obtuvieron más de 70 o igual.
	•	Obtenga la cantidad de estudiantes e imprímalo, no hacerlo manual.
	•	Indicar la cantidad de personas que obtuvieron una nota menor a 70.
	•	Obtener la nota máxima y el nombre del estudiante e imprimirla.
	•	Obtener la nota mínima y el nombre del estudiante e imprimirla.
"""

from heapq import nlargest


lista_de_notas = {
 "maria" : 70,
"jose" : 55,
"jenny" : 99,
"juanita" : 88,
"pedro" : 89,
"sofia" : 100,
"valeria" : 24,
"fernanda" : 67,
"julian" : 55,
"oscar" : 99

 }
#for clave in lista_de_notas: 
#    print (clave,":", lista_de_notas[clave])

for clave, valor in lista_de_notas.items(): 
    print(clave, ":", valor)

#alumnos_aprobados = nlargest(5, lista_de_notas, keys=lista_de_notas.get)
#print(alumnos_aprobados)

#notaminima = lista_de_notas.keys () 
#if notaminima >= 70:
#    print (lista_de_notas.keys())

#talvez no se ha visto pero aprendi que es un iterador y min y max sirve sobre cualquier objeto iterable
nota_maxima = max(zip(lista_de_notas.values(), lista_de_notas.keys()))
print (nota_maxima)

nota_minima = min(zip(lista_de_notas.values(), lista_de_notas.keys()))
print (nota_minima)

    


