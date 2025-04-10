texto = "arquitectura"
vocal ="aeiou"
contador = 0
for letra in texto:
    if letra in vocal:
        contador += 1
print ("cantidad de vocal", contador)


for i in range (21): #desde el 0 hasta el 21 inclusive
    if i % 2 == 0:
        print(i)

contra="uca"
entrada=""
intentos=0
while entrada!=contra and intentos < 3:
    entrada=input("ingrese su contraseña")
    if entrada!= contra:
        print("incorrecta")
        intentos +=1
if entrada == contra:
    print("correcta")
else:
    print("no hay mas intentos")



