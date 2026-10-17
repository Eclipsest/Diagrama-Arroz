print ("Los ingredientes para hacer el arroz son: arroz,agua,aceite y sal")
print ("Los utensilios a usar son: olla con tapa, taza medidora, cuchara y colador")

print ("Reune los ingredientes y utensilios")
print ("Poner el arroz en el medidor")
print ("Medir el arroz")
print ("lavar el arroz")
lavararroz= input ("EL arroz ya no tiene casi almidon? (si/no)")
while lavararroz == "no":
    print("Lavar el arroz de nuevo")
    lavararroz = input("¿El arroz ya no tiene casi almidón? (si/no): ")

if lavararroz == "si":
    print("Escurrir bien el arroz")

print ("Prender el fogon y poner la olla en el fogon")
print ("agregar aceite")
print ("Agregar el arroz a la olla")
print ("revolver durante 1 a 2 minutos")
print ("Agregar el agua a la olla")

cantagua = input ("La cantidad de agua es la correcta? (si/no)")
if cantagua == "si":
    print("Subir el fuego")
while cantagua == "no":
    print("Agregar mas agua")
    cantagua = input("¿La cantidad de agua es la correcta? (si/no): ")

hervir = input ("El agua ya esta hirviendo? (si/no)")
while hervir == "no":

    print("Suba el fuego y espere a que hierva")
    hervir = input("¿El agua ya está hirviendo? (si/no): ")
if hervir == "si":
    print("Bajar el fuego y tapar la olla")
    print("Esperar 15 minutos")

tierno= input ("El arroz ya esta tierno? (si/no)")
while tierno =="no":
    agua= input("¿aun hay agua en la olla? (si/no): ")
    if agua == "no":
        print("Agregar mas agua")
        agua = input("¿aun hay agua en la olla? (si/no): ")
    if agua == "si":
        print("Subir el fuego y esperar a que hierva")
        tierno= input ("El arroz ya esta tierno? (si/no): ")
if tierno =="si":
    print("Apagar el fuego")

print("Dejar reposar el arroz durante 5 minutos")
print ("soltar los granos de arroz con un tenedor")
print ("Servir")
