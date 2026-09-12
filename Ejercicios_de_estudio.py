
"""
numero = int(input("Ingrese un número: "))

if numero % 2 == 0:
    print ("El número es par")
else:
    print ("El número es impar")"""
    
    
"""nombre = input("cual es tu nombre: ")
edad = int(input("cual es tu edad: ")) 
print("tu nombre es " + nombre)
print(f"tu nombre es {nombre} y tienes {edad} años")"""

"""edad = int(input("ingresa tu edad: "))

if edad >= 65:
    print("eres un adulto mayor")
elif edad >= 18:    
    print("es mayor de edad")      
else:
    print("eres menor de edad")"""
        
"""pg13 = 13

edad = int(input("ingresa la edad del espectador: ")) 

if edad >= pg13:
    print("estas autorizado para ver la pelicula") 
else:
    print("no estas autorizado, eres menor de edad")  """ 
    
"""Es mayor o igual a 90, la calificación es "A".
Está entre 80 y 89, la calificación es "B".
Está entre 70 y 79, la calificación es "C".
Está entre 60 y 69, la calificación es "D".
Es menor que 60, la calificación es "F".  """ 
           
"""Nota = int(input("ingrese la calificacion del estudiante: "))

if Nota >= 90:
    print("su calificacion es A")
elif Nota >= 80:
    print("su calificacion es B")    
elif Nota >= 70:
    print("su calificacion es C")               
elif Nota >= 60:
    print("su calificacion es D") 
else:
    print("su calificacion es F y usted esta desaprobado")       """
    
"""# 1. Solicitamos los tres números al usuario
num1 = float(input("Ingresá el primer número: "))
num2 = float(input("Ingresá el segundo número: "))
num3 = float(input("Ingresá el tercer número: "))

# 2. Comparamos los números entre sí para encontrar el mayor
if num1 >= num2 and num1 >= num3:
    mayor = num1
elif num2 >= num1 and num2 >= num3:
    mayor = num2
else:
    mayor = num3

# 3. Mostramos el resultado
print(f"El número mayor es: {mayor}")    """

"""contador = 1

while contador <=5:
    print(contador)
    contador += 1"""
    
"""contador = 1

while True:
    print("el contador es:", contador)
    contador += 1
    if contador > 5:
        break    """
    
"""for i in range(1,6):
    print(i)    """
    
"""numero = 1
while numero <= 10:
    print(numero)
    numero += 1    """
    
"""frutas = ("manzana", "banana", "pera", "frutilla", "sandia")

for i in frutas:
    print(i)"""    
    
"""nombre = input("ingresa tu nombre: ")

for i in nombre:
    print(i)    """
    


"""while True:
    numero =  int(input("ingresa un numero: "))   
    print(numero)
    if numero < 0:
        break"""
        
"""contraseña = 1234

while True:
    Password = int(input("ingresa tu Contraseña: "))
    if Password == contraseña:
        break 
print("la contraseña es correcta")  """        
    
    
"""numero = int(input("ingresa el numero de la tabla para multiplicar"))

for i in range(1,11):
    resultado = numero * i
    print(f"{numero} X {i} = {resultado}")"""
     
     
"""def saludar(nombre):
    return "¡Hola, " + nombre + "!"

print(saludar("Mario"))    
print(saludar("Lucas")) 
print(saludar("Cristina"))
print(saludar("34"))"""
       
       
"""def presentar(nombre: str, edad: int) -> str:
    return f"Hola, mi nombre es {nombre} y tengo {edad} años."

# Ejemplo de uso
mensaje = presentar("Ana", 30)
print(mensaje)  # Output: Hola, mi nombre es Ana y tengo 30 años."""

"""def add_numbers(a, b):
    return a + b

result = add_numbers(2000, 894)
print(result)  # Output: 8"""

"""def promedio(a, b, c):
    return (a + b + c) / 3

result = promedio(8, 9, 5)
print(result)  """

"""def describe_persona(name, age):
    return f"Name: {name}\nAge: {age}"

# Uso de la función
resultado = describe_persona(age=25, name="John")
print(resultado)"""

"""def calculate_total(*args):
    total = sum(args)
    return total

result = calculate_total(2,4,6,8,5,8,2)
print(result)  
# Output: 20"""

"""def area_rectangulo(ancho: float, alto: float) -> float:
    return ancho * alto

# Ejemplo de uso
ancho_rect = float(input("ingresa el ancho del rectangulo: "))
alto_rect = float(input("ingresa el ancho del rectangulo:  "))

area = area_rectangulo(ancho_rect, alto_rect)
print(f"El área del rectángulo es: {area}")"""

"""def imprimir_mensaje(): 
   print("msg")
   
imprimir_mensaje()   """

"""def contar_hasta_cero(n):
    if n <= 0:  
        # Caso base
        print("¡Boom!")
    else:  
        # Caso recursivo
        print(n)
        contar_hasta_cero(n - 1)  

contar_hasta_cero(900)
"""

"""def contar(numero):
    if numero == 0:  
        # Caso base: número es cero
        return
    else:  
        # Caso rec: contar uno por uno
        print(numero)
        contar(numero - 1)


contar(5)"""


"""Crear una función que eleve un número al cuadrado y lo imprima."""

"""def potencia(numero: int):
    resultado = numero ** 2
    return resultado
    
print(potencia(6)) 
   """
   
"""Crear una función que calcule el IVA de un producto y lo imprima con la leyenda 
“El IVA correspondiente al (valor ingresado) es (resultado de la función).   """

"""def IVA(total: float):
    iva = total * 0.21
    return iva


compra_total = float(input("ingrese el monto total de la compra:  "))

print(f"El IVA correspondiente al monto $ {compra_total:.2f}  es de $ {IVA(compra_total):.2f}")
"""

"""Situación: El programa debe simular un menú bancario
simple.
Mostrar el siguiente menú al usuario:
1. Ver saldo
2. Realizar transferencia
3. Salir
El usuario debe ingresar un número del 1 al 3 según la opción
que quiera. El programa mostrará un mensaje correspondiente:
● Si elige 1 → mostrar "Su saldo es $15.000"
● Si elige 2 → mostrar "Transferencia realizada con éxito"
● Si elige 3 → mostrar "Saliendo del sistema..."
● Si elige otro número → mostrar "Opción inválida"""



"""print("---MENU PRINCIPAL---")
print("Opcion 1: Ver saldo")
print("Opcion 2: Realizar transferencia")
print("Opcion 3: Salir del Sistema")

opcion = int(input("Ingrese la Opcion Solicitada: "))

while True:
   
    if opcion == 1:
             print("Su saldo es $15.000")
             opcion = int(input("Ingrese la Opcion Solicitada: "))
    elif opcion == 2:
            print("Transferencia realizada con éxito")
            opcion = int(input("Ingrese la Opcion Solicitada: "))
    elif opcion == 3:
            print("Saliendo del sistema...")
            break
    else:
            print("Opción inválida")
            opcion = int(input("Ingrese la Opcion Solicitada: "))"""



"""notas = [[6, 7], [8, 9], [10, 6]]

for fila in notas:
    for valor in fila:
        print(valor)"""
        
"""torneo = [ [[1,2], [3,4]], [[5,6], [7,8]] ]
print(torneo[1][1][0])  # ¿Qué imprime?

frutas = ["manzana", "banana"]
frutas.append("pera")
print(frutas)
    
    
tareas = ["leer", "escribir", "revisar"]
tareas[1] = "resumir"
print(tareas)

coordenadas = (10, 20)
print(coordenadas[0])


nombres = {"Ana", "Luis", "Ana", "Carlos"}
print(nombres)


nombres = ["Ana", "Luis", "Ana", "Carlos"]
unicos = set(nombres)
print(unicos)"""

"""datos = {"nombre": "Lucia", "edad": 25}
datos["ciudad"] = "Rosario"
print(datos["ciudad"])

print(datos)"""

"""#Usando sorted
lista_original = [3,1,4,1,5,9,2,6]
sorted_list = sorted(lista_original)
print(sorted_list)
print(lista_original)

print("otra prueba")

#Usando sort
lista_original = [3,1,4,1,5,9,2,6]
print(lista_original)
lista_original.sort()
print(lista_original)

print("desendente")

#Con sorted
lista_original = [3,1,4,1,5,9,2,6]
descendente = sorted(lista_original, reverse=True)
print(lista_original)
print(descendente)
print(lista_original)

#Con sort
print("con sort")
lista_original.sort(reverse=True)
print(lista_original)"""

"""
numeros = [5, 2, 9, 1, 5, 6]
ordenada = sorted(numeros)
print(ordenada)

descendente = sorted(numeros, reverse=True)
print(descendente)

"""

"""cadenas = ["pera", "manzana", "banano", "cereza"]
alfabetica = sorted(cadenas)
print(alfabetica)"""


"""# Tu lista original
tuplas = [(1, "d"), (3, "b"), (2, "a"), (5, "c")]

# 1. Ordenar en orden ascendente por el segundo elemento
# Usamos lambda x: x[1] para indicar que ordene por el índice 1 (el segundo elemento)
tuplas_ascendente = sorted(tuplas, key=lambda x: x[1])

# 2. Ordenar en orden descendente por el segundo elemento
# Solo agregamos el argumento reverse=True
tuplas_descendente = sorted(tuplas, key=lambda x: x[1], reverse=True)

# Resultados
print("Lista original:   ", tuplas)
print("Ascendente (a-z): ", tuplas_ascendente)
print("Descendente (z-a):", tuplas_descendente)"""

"""Dada una lista de diccionarios, ordénalos por un valor específico de una clave en orden ascendente.

Luego, ordénalos en orden descendente."""

"""diccionarios = [ {"nombre": "Juan", "edad": 25}, {"nombre": "Ana", "edad": 22}, {"nombre": "Luis", "edad": 30}, {"nombre": "Maria", "edad": 28} ]

dic_asc = sorted(diccionarios, key=lambda x: x["edad"] )

dic_des = sorted(diccionarios, key=lambda x: x["edad"], reverse=True )

print(dic_asc)

print(dic_des)"""


"""for i in range(5):
    nombre = input(f"Ingrese el nombre #{i + 1}: ")
    print(f"Hola, {nombre}!")"""


"""suma = 0
for i in range(4):
    nota = float(input(f"Ingrese la nota #{i + 1}: "))
    suma += nota
    promedio = suma / 4
print("El promedio es:", promedio)"""


"""def mostrar_menu():
    print("-----Menú de opciones-----")
    print("1. Ver datos")
    print("2. Modificar datos")
    print("3. Salir")

while True:
    mostrar_menu()
    opcion = int(input("elige una opcion: "))
    if opcion == 1:
        print("Mostrando Datos")
    elif opcion == 2:
        print("Modificando Datos") 
    elif opcion == 3:
        print("Saliendo del Sistema")
        break
    else:
        print("Opcion Invalidad")"""
        
        
""" DICCIONARIOS"""       
        
        
"""alumno = {'Nombre' : 'Juan', 'edad' : 25, 'ciudad' : 'Rio Grande', 'carrera' : 'Ciencia de datos'}

for i in alumno:
    print(f"nombre : {alumno['Nombre']}")
    print(f"edad : {alumno['edad']}")
    print(f"carrera : {alumno['carrera']}")"""
    
    

    
alumno = { "nombre": "Juan",
          "edad": 23,
          "carrera": "Ciencia de Datos",
          "ciudad": "Río Grande"
          }
 
for clave, valor in alumno.items():
    print(clave, ":", valor)
       
        
        
               