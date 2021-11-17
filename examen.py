import pandas as pd

conversiones = pd.read_csv("conversiones.csv", sep = ";")
navegacion = pd.read_csv("navegacion.csv", sep = ";")

print(conversiones)
print(navegacion)