import pandas as pd
import numpy as np

datos={
    "titulo":["Inception","Avengers:EndGame","Parasite", "Toy Story","Superman","Cómo entrenar a tu dragón"],
    "año":[2019,2020,2008,2019,2025,2025],
    "recaudacion":[836, 2798, 266, 1005, 1073,1234],
    "duracion_min":[148,200,239,283,230,123]
}
df_peliculas= pd.DataFrame(datos)
peliculas_recaudacion= df_peliculas[df_peliculas["recaudacion"]>1000]
recaudacion_total= np.sum( df_peliculas["recaudacion"])#RECAUDACIÓN TOTAL
duracion_promedio= np.mean(df_peliculas["duracion_min"])
peliculas_2019= df_peliculas.groupby("año").get_group(2019)
print(df_peliculas.sort_values("duracion_min", ascending=True))
#print("La duración promedio es: ",duracion_promedio)
#print("La recaudación total es. ",recaudacion_total)
#print(peliculas_2019)
#print(peliculas_recaudacion)
#print(df_peliculas)
#print(df_peliculas.head())

