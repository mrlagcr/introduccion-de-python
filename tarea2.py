"""
	•	Investigue como recorrer un diccionario y en un archivo nuevo llamado tarea2.py 
    demuestre con código como recorrer el siguiente diccionario y 
    que imprima de forma dinámica sus llaves y sus valores uno por uno:

diccionario_con_cosas = {
    0 : "Monitor",
    "uno" : "Teclado",
    "dos" : "100"
}
"""
opcion = str(input ("Deseas ingresar a diccionario: "))
while opcion == "si":
    print ("adelnate");
    print("Las Claves son: ")
    break
else:
    print("Muchas gracias")
    quit()
#lo anterior esta fuera de la tarea solo queria divertirme un poco, queria aprender a frenar un bucle
# y a frenar una ejecuacion del codigo. 
#puse primero el diccionario para que
#me desplegara la lista de opciones que tenia con for
diccionario_con_cosas = {
    0 : "Monitor",
    "uno" : "Teclado",
    "dos" : "100"
}
for clave in diccionario_con_cosas:
        print (clave)
#aca puse un input con el fin de dejar al usuario buscar el valor que necesitaba
#clave por clave
opcion = input ("Ingresa la clave del valor que necesitas: ")
#use la opcion de str por que se que 0 es entero y me daria error por se un datos 
#diferente a "uno" y "dos".
if opcion == str(0):
    print(diccionario_con_cosas.get(0))
elif opcion == "uno":
    print (diccionario_con_cosas.get("uno"))
elif opcion == "dos":
        print (diccionario_con_cosas.get("dos"))
else:
    print ("valor no encontrado")

print ("Muchas Gracias por accesar al diccionario de cosas")

#Me tomo toda la tarde, es que tambien estoy tomando por cuenta propia c++ y me acorde de switch
#en ese leguaje y busque algo parecido pero en python y me tope con el elif 
#tambien ya habia trabajo con el input antes de entrar a este curso y aproveche ese conocimiento 



