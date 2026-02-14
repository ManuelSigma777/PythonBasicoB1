#Loops
mi_lista = [1,2,3,4,5]

for i in mi_lista:
    print("El numero es:",i)

    resultado = 0
    for i in mi_lista:
        resultado += i

        print(f"El resultado de la suma de mi lista es: {resultado}")

        for i in range(2, 9):
            print(i)
        
        mi_lista_2 = ["Lunes","Martes","Miercoles","Jueves","Viernes"]
        for i in mi_lista_2:
            if i != "Lunes":
                print(f"Feliz {i}!")

#while loop
i=0

while i < 5:
    i += 1 
    if i ==3:
        continue
    print(i)
    if i == 4:
        break
else:
    print("i es igual o mayor a 5")

#Practica 2
# Dada la lista mi_lista_2 = ["Lunes","Martes","Miercoles","Jueves","Viernes"]
#imprimir cada elemento e la lista 3 veces y cuando sea lunes no lo incluyas
# Usa los loop while y for
# REsultados
#Martes
#Miercoles
#Jueves
#Viernes
#Martes
#Miercoles
#Jueves
#Viernes
#Martes
#Miercoles
#Jueves
#Viernes
i=0
mi_lista_2 = ["Lunes","Martes","Miercoles","Jueves","Viernes"]
while i < 3:
    i += 1 
    for d in mi_lista_2:
            if d != "Lunes":
                print(f"{d}!")