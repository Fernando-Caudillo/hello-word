#cadena = input("Introduzca una cadena: ")
#print(cadena.lower())
#print(cadena.upper())
#print(cadena.title())


#cadena = input("Introduzca una cadena: ")
#numi = input("Introduzca un numero inicial: ")
#numf = input("Introduzca un numero final: ")
#nueva = cadena[5:13]
#print(cadena[int(numi):int(numf)])
#print(nueva)

#myFruitList = ["apple", "banana", "cherry"]
#fruit = input("Ingrese una fruta: ")
#myFruitList.append(fruit)
#print(myFruitList)

#colors = []
#colores = input("Ingrese colores separados por coma: ")
#colors = colores.split(',')
#print(colors)


#word = []
#wordus = input("Ingrese una palabra: ")
#word = list(wordus)
#print(word)

#FruitDictionary = {
 #"naranja" : "orange",
 #"platano" : "banana",
 #"manzana" : "apple"
 #}
#fruta = input("Digite una fruta: ")
#print(FruitDictionary.get(fruta.lower(), "No tenemos esa fruta"))
 
#ValorEncontrar = input("Ingrese el clinete que deseas buscar: ")
#numero = [124, 243, 4234, 323423, 234325, 238, 236]
#encontrado = False

#for n in numero:
# if n == int(ValorEncontrar):
#  encontrado = True
#  break

#if encontrado:
# print("El cliente existe")
#else:
# print("No se encontro el cliente")



    
def stamps():
  print("We have many stamp designs to choose from.")

def envelope():
  print("We have many envelope sizes to choose from.")

def copy():
  copies = input("How many copies would you like? (Enter a number) ")
  print("Here are {} copies.".format(copies))
  
opciones = {
  'stamps' : stamps,
  'envelope' : envelope,
  'copy' : copy,
 }

userReply = "stamps"
#userReply = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ")
print(opciones.get(userReply, "Thank you, please come again."))




