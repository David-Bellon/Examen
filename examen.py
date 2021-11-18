import re
from numpy import shares_memory
import pandas as pd

conversiones = pd.read_csv("conversiones.csv", sep = ";")
navegacion = pd.read_csv("navegacion.csv", sep = ";")

index = []
for i in range(conversiones.shape[0]):
    if conversiones._get_value(i, "id_user") == "None":
        index.append(i)

conversiones = pd.DataFrame(conversiones.drop(conversiones.index[index]), columns = conversiones.columns)
conversiones = conversiones.reset_index()

#Numero de visitas que recibe el cliente
print("El numero de visitas que recibe es:", navegacion.shape[0], "visitas")

#Cuántas de ellas convierten y cuántas no (en %)
convertidos = 0
users_navegacion = navegacion["id_user"]
users_conversion = conversiones["id_user"]
for user_nav in users_navegacion:
    for user_conv in users_conversion:
        if user_nav == user_conv:
            convertidos += 1

print("El porcentaje de visitas a convertidos es de " , convertidos / navegacion.shape[0] * 100, end="%\n")

#Por tipo de conversión (CALL o FORM), ¿cuántas hay de cada una?
#Primero observamos que no hay ningun user repetido, a simple vista se ve
call = 0
form = 0
tipo = conversiones["lead_type"]
for type in tipo:
    if type == "CALL":
        call += 1
    else:
        form += 1

print("EL numero de conversiones del tipo call es:", call)
print("EL numero de conversiones del tipo form es:", form)

#Porcentaje de usuarios recurrentes sobre el total de usuarios
#Solo nos interesa una vez cada uno de los users asi que los guardamos en un conjunto para que no haya repetidos
recurrente = {()}
number_of_users = {()}

for i in range(navegacion.shape[0]):
    number_of_users.add(navegacion._get_value(i, "id_user"))
    if navegacion._get_value(i, "user_recurrent") == True:
        recurrente.add(navegacion._get_value(i, "id_user"))
print("El porcentaje de usuarios recurrentes frente a los totales es de:", len(recurrente) / len(number_of_users) * 100, end="%\n")

#Unir a la tabla de navegacion si convierte o no.
data = []
only_user = navegacion["id_user"]
for user in only_user:
    convierte = False
    for i in conversiones["id_user"]:
        if user == i:
            convierte = True
    
    if convierte:
        data.append(1)
    else:
        data.append(0)

navegacion["convierte"] = data
#Ahora navegacio contiene todos los datos de si ese usuario convierte o no.

#Ver cual es el coche más visitado de la página.
cars = {
    
}

for i in range(navegacion.shape[0]):
    m = re.search("http(?:s?):\/(?:\/?)www\.metropolis\.com\/es\/(.+?)\/.*", str(navegacion._get_value(i, "url_landing")))
    if m != None:
        if m.groups()[0] in cars:
            cars[m.groups()[0]] += 1
        else:
            cars[m.groups()[0]] = 1
        
for car in cars.keys():
    print("El coche", car, "ha sido buscado", cars[car], "veces")