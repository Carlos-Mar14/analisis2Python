import pandas as pd
from data.data1 import apartamento1, apartamento2
from helpers.crearTablasHTML import crearTabla


#Creamos el dataframe
tabla1=pd.DataFrame(apartamento1, columns=['edad'])
tabla2=pd.DataFrame(apartamento2, columns=['edad'])
tabla3=pd.read_csv("./data/empleados.csv")

#Filtrando o Aplicando condiciones a mi dataframe
#1. Orientada a la logica de consultas (queries)
#EmpleadosJovenes1=tabla3.query('edad < 28 and cargo=="analista1"')
#print(EmpleadosJovenes1)


#2. Orientada al dataframe
#EmpleadosJovenes2=tabla3[(tabla3['edad']<28) & (tabla3['cargo']=="analista1")]
#print(EmpleadosJovenes2)

#Creando la tabla
#crearTabla(EmpleadosJovenes1, "tabla")

# datosEstadisticosApto1=tabla1.describe()
# datosEstadisticosApto2=tabla2.describe()
# datosEstadisticosEmpresa=tabla3.describe()

# print(datosEstadisticosApto1, "\n")
# print(datosEstadisticosApto2, "\n")
# print(datosEstadisticosEmpresa, "\n")


#Filtrando o Aplicando condiciones a mi dataframe
analista1=tabla3.query('cargo=="analista1"')
analista2=tabla3.query('cargo=="analista2"')
jubilados=tabla3.query('edad>= 50')
#print(jubilados)

#Generemos tablas para el reporte
crearTabla(analista1, "analistas1")
crearTabla(analista2, "analistas2")
crearTabla(jubilados, "jubilados")