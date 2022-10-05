"""
Tiene los siguientes dos tipos de datos completos:

Tupla_con_cosas = ("zapatos", "Mouse", "jamón", 56)

diccionario_con_cosas = {
    0 : "Monitor",
    "uno" : "Teclado",
    "dos" : "100"
}
Indicaciones:
1.	Imprima el índice 3 de la tupla.
2.	Imprima el valor de la llave “dos”.
3.	Sume, reste, multiplique, divida los datos que imprimió anteriormente y muestre su resultado.
"""
tupla_cosas = ("zapatos", "Mouse", "Jamon", 56);

diccionario_con_cosas ={

0: "Monitor",
"uno": "Teclado",
"dos": "100"
}


#Indicaciones
#1)
print(tupla_cosas[3])

#2)
print(diccionario_con_cosas.get("dos"))


#3)
suma = int(diccionario_con_cosas.get("dos")) + tupla_cosas[3]
resta = int(diccionario_con_cosas.get("dos")) - tupla_cosas[3]
multiplicacion = int(diccionario_con_cosas.get("dos")) * tupla_cosas[3]
division = int(diccionario_con_cosas.get("dos")) / tupla_cosas[3]


print("el resultado de suma es: ", suma)
print("el resultado de resta es: ", resta)
print("el resultado de multiplicacion es: ", multiplicacion)
print("el resultado de division es: ", division)


