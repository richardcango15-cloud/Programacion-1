### clase 3 aqui trabajaremos con variables###

#Listas de frutas
frutas=["Manzanas", "Fresas", "Uvas"]
print(frutas)
numeros= (10,20,30,40)
print(numeros)

#aceder a elemnetos de las listas
print(frutas[0])
print(frutas[1])
print(frutas[2])
#print(frutas[3]) ERROR

#agregar elementos
frutas.append("Banana") #agrega al fiinal de la lista
print(frutas)

frutas.insert(0,"Mango") #insertar en una pocision especifica
print(frutas)

##Modificar elemento
frutas[1]="Quiwis"
print(frutas)

###Eliminar elemento
frutas.remove("Uvas")  #Indicar el elemento
print(frutas)