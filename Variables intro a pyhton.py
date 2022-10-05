
#variableas


from ast import If


myvariable = "my string variable"
print(myvariable)

"""
variale se menciona de cualquier forma. 
pero de forma correcta es my_variable.
"""
mi_int_variable = 30
print (mi_int_variable)

variable_bool = False
print(variable_bool)

#str es una funcion que convierte algo numerico a cadena de texto
mi_int_to_str_variable = str(mi_int_variable)
print (mi_int_to_str_variable)
print (type(mi_int_to_str_variable))

#diferecntes argumentos o variables separados por coma
#concatenacion de cadenas, se conoce asi
print(myvariable, mi_int_variable, mi_int_to_str_variable, variable_bool)

# algunas funciones del sistema
print(len(mi_int_to_str_variable))
print(len(myvariable))

#los print tambien pueden recibir parametros
print("este es el valor de:",variable_bool)

#variables en una sola linea
name, surname, alias, age = "Brian", "Corrales", "Mrlagacr", 30
print("mellamo:",name, ",mi apellido es:",surname, ",me conocen como:",alias)

#variables que solicitan datos
first_name = input("cual es tu nombre?:")
print ("hola,",first_name)

age = int(input("que edad tienes?:"))

if age > 29: 
    print ("estas muy roco")
else:
    print ("estas muy joven")

#Forzar el tipo
address : str = "direccion" 
address = 32 
print (address)
#esto asi, hace una sobreescrito 


