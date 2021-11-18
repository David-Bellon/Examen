import pandas as pd
from pandas.core.indexing import convert_missing_indexer

conversiones = pd.read_csv("conversiones.csv", sep = ";")
navegacion = pd.read_csv("navegacion.csv", sep = ";")

index = []
for i in range(conversiones.shape[0]):
    if conversiones._get_value(i, "id_user") == "None":
        index.append(i)

conversiones = pd.DataFrame(conversiones.drop(conversiones.index[index]), columns = conversiones.columns)
conversiones = conversiones.reset_index()
print(conversiones)
