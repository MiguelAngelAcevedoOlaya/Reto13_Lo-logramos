# The last dance

### Punto 1

Soy un bonito que hace todo

```
def escoger_valores(valor):
  bandera = True
  while bandera == True:
    if valor in range(1,4):
      break
    else:
      print("INGRESE VALOR entre uno y tres")
      valor = int(input("Ingresa 1 si quieres elementos elementos de texto \nIngresa 2 si quieres números enteros \nIngresa 3 si quieres flotantes \n "))
  return valor

def crear_diccionario(num_elementos):
  dic = {}
  for i in range(num_elementos):
    key = input("Ingresa el valor del key: ")
    bandera = True
    while bandera == True:
      if key in dic:
        print("ingresa otro valor, que ese ya esta")
        key = input("Ingresa el valor del key, lo haremos con nímeros para ordenar mas cheverongo: ")
      else:
        break
    if valor == 1:
      valores = input("Ingresa lo  que desees, recuerda que es string: ")
    elif valor == 2:
      valores = int(input("Ingresa lo  que desees, recuerda que es entero: "))
    elif valor ==3:
      valores = float(input("Ingresa lo  que desees, recuerda que es flotante: "))
    dic[key] = valores
  return dic

def orden_dic():
  orden = dict(sorted(elem.items(), key=lambda item:item[1]))
  return orden

if __name__ == "__main__":
  num_elementos = int(input("Ingrese cuantos elementos deseas agregar al dicionario: "))
  valor = int(input("Ingresa 1 si quieres elementos elementos de texto \nIngresa 2 si quieres números enteros \nIngresa 3 si quieres flotantes \n "))
  elem = crear_diccionario(num_elementos)
  val = escoger_valores(valor)
  orden = orden_dic()
  print("EL numero de elementos del diccionario sera de:" +str(num_elementos))
  print("Has escogido la opción: " +str(valor))
  print("Tu diccionario es: ")
  print(elem)
  print("La lista ordenada: ")
  print(orden)

```

### Punto 2

COMO ERA OPCIONAL ES UN PLACER VER ESTO

```
def diccionario(num_elementos):
  dic = {}
  for i in range(num_elementos):
    key = input("Ingresa el valor del key: ")
    bandera = True
    while bandera == True:
      if key in dic:
        print("ingresa otro valor, que ese ya esta")
        key = input("Ingresa el valor del key:: ")
      else:
        break
    valor = int(input("Ingresa 1 si quieres elementos elementos de texto \nIngresa 2 si quieres números enteros \nIngresa 3 si quieres flotantes \n "))
    while bandera == True:
      if valor in range(1,4):
        break
      else:
        print("INGRESE VALOR entre uno y tres")
        valor = int(input("Ingresa 1 si quieres elementos elementos de texto \nIngresa 2 si quieres números enteros \nIngresa 3 si quieres flotantes \n "))
    if valor == 1:
      valores = input("Ingresa el texto que desees, los números son menores que las letras, van bajo una regla extraña, mejor texto ")
    elif valor == 2:
      valores = int(input("Ingresa el número que desees ingregasr como valor correspondinete a la llave: "))
    elif valor == 3:
      valores = float(input("Ingresa el flotante que desees ingregasr como valor correspondinete a la llave: "))
    dic[key] = valores
  return dic

def crear_dic():
  dic_3 = {}
  bandera = True
  while bandera == True:
    for k,v in dic_1.items():
      if k in dic_3:
        continue
      else:
        dic_3[k] = v
    for k,v in dic_2.items():
      if k in dic_3:
        continue
      else:
        dic_3[k] = v
    bandera = False
    return dic_3


  return dic_3

if __name__ == "__main__":
  num_elementos = int(input("Cuantos elementos quieres para el diccionario 1: "))
  dic_1 = diccionario(num_elementos)
  print("Primer diccionario es: " +str(dic_1))
  num_elementos_b = int(input("Cuantos elementos quieres para el diccionario 2: "))
  dic_2 = diccionario(num_elementos_b)
  print("Segundo diccionario es: " +str(dic_2))
  tercer_dic = crear_dic()
  print("El diccionar junto es: " +str(tercer_dic))

```

### Punto 3

```
import json

with open('archivo.json', "r") as readFile:
  data = json.load(readFile) # Leer archivo

ingresa_ = input("Ingresa un deporte: ") # Pregunta deporte
ingresa_ = ingresa_.capitalize()
if ingresa_ == "futbol" or ingresa_ =="Futbol": # Casos especiales
  ingresa_ = "Fútbol"
if ingresa_ =="Bascket" or ingresa_ == "bascket":
  ingresa_ = "Baloncesto"

for persona, detalles in data.items(): #Busca e imprime usando for
  for uno, dos in detalles.items():
    if "deportes" in uno:
      for i in dos:
        if i == ingresa_:
          for tres, cuatro in detalles. items():
            if 'nombres' in tres:
              for cinco, seis in detalles.items():
                if 'apellidos' in cinco:
                  print("La persona " +str(cuatro)+ "" +str(seis)+ " juega " +str(ingresa_))

ingresa = int(input("Ingresa un número de edad: ")) # Ingresar edad
ingresa_2 = int(input("Ingresa otro númeor de edad: ")) # Ingresar edad 2

for persona, detalles in data.items(): #Busca e imprime usando for
  for uno, dos in detalles.items():
    if "edad" in uno:
      if ingresa > ingresa_2:
        if dos <= ingresa and dos >= ingresa_2:
          for tres, cuatro in detalles. items():
            if 'nombres' in tres:
              for cinco, seis in detalles.items():
                if 'apellidos' in cinco:
                  print("La persona " +str(cuatro)+ "" +str(seis)+ " esta entre " +str(ingresa_2)+ " y " +str(ingresa)+ " años")
      if ingresa < ingresa_2:
        if dos >= ingresa and dos <= ingresa_2:
          for tres, cuatro in detalles. items():
            if 'nombres' in tres:
              for cinco, seis in detalles.items():
                if 'apellidos' in cinco:
                  print("La persona " +str(cuatro)+ "" +str(seis)+ " esta entre " +str(ingresa)+ " y " +str(ingresa_2)+ " años")
      if ingresa == ingresa_2:
        if dos == ingresa and dos == ingresa_2:
          for tres, cuatro in detalles. items():
            if 'nombres' in tres:
              for cinco, seis in detalles.items():
                if 'apellidos' in cinco:
                  print("La persona " +str(cuatro)+ "" +str(seis)+ " tiene " +str(ingresa)+ " años")
```

### Punto 4

Manipulamos el archivo y utilizando ciclos for, buscano variables parecidad a las solicitados y usando la función que pase de UTC a hora normal

```
import json # Json
from datetime import datetime, timezone # Fecha
from pprint import pprint # Imprimir bonito

# Cargar archivo
jsonString = '''
{\"dt\": {\"0\": 1685116800, \"1\": 1685203200, \"2\": 1685289600, \"3\": 1685376000, \"4\": 1685462400, \"5\": 1685548800, \"6\": 1685635200, \"7\": 1685721600}, \"sunrise\": {\"0\": 1685097348, \"1\": 1685183745, \"2\": 1685270143, \"3\": 1685356542, \"4\": 1685442942, \"5\": 1685529342, \"6\": 1685615743, \"7\": 1685702145}, \"sunset\": {\"0\": 1685143042, \"1\": 1685229458, \"2\": 1685315875, \"3\": 1685402291, \"4\": 1685488708, \"5\": 1685575124, \"6\": 1685661541, \"7\": 1685747958}, \"moonrise\": {\"0\": 1685118300, \"1\": 1685207460, \"2\": 1685296620, \"3\": 1685385720, \"4\": 1685474880, \"5\": 1685564220, \"6\": 1685653740, \"7\": 1685743500}, \"moonset\": {\"0\": 0, \"1\": 1685164320, \"2\": 1685253000, \"3\": 1685341560, \"4\": 1685430120, \"5\": 1685518740, \"6\": 1685607600, \"7\": 1685696640}, \"moon_phase\": {\"0\": 0.22, \"1\": 0.25, \"2\": 0.28, \"3\": 0.31, \"4\": 0.35, \"5\": 0.38, \"6\": 0.41, \"7\": 0.45}, \"pressure\": {\"0\": 1011, \"1\": 1012, \"2\": 1012, \"3\": 1012, \"4\": 1012, \"5\": 1012, \"6\": 1012, \"7\": 1011}, \"humidity\": {\"0\": 85, \"1\": 61, \"2\": 68, \"3\": 74, \"4\": 84, \"5\": 66, \"6\": 81, \"7\": 82}, \"dew_point\": {\"0\": 23.93, \"1\": 22.5, \"2\": 23.67, \"3\": 23.35, \"4\": 24.22, \"5\": 22.73, \"6\": 23.18, \"7\": 22.93}, \"velViento\": {\"0\": 3.56, \"1\": 5.07, \"2\": 5.38, \"3\": 3.95, \"4\": 4.74, \"5\": 3.75, \"6\": 4.08, \"7\": 5.94}, \"dirViento\": {\"0\": 188, \"1\": 14, \"2\": 21, \"3\": 23, \"4\": 40, \"5\": 330, \"6\": 176, \"7\": 168}, \"wind_gust\": {\"0\": 6.47, \"1\": 8.86, \"2\": 8.95, \"3\": 6.12, \"4\": 7.17, \"5\": 5.4, \"6\": 5.13, \"7\": 9.67}, \"weather\": {\"0\": [{\"id\": 501, \"main\": \"Rain\", \"description\": \"lluvia moderada\", \"icon\": \"10d\"}], \"1\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"2\": [{\"id\": 501, \"main\": \"Rain\", \"description\": \"lluvia moderada\", \"icon\": \"10d\"}], \"3\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"4\": [{\"id\": 501, \"main\": \"Rain\", \"description\": \"lluvia moderada\", \"icon\": \"10d\"}], \"5\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"6\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"7\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}]}, \"clouds\": {\"0\": 100, \"1\": 82, \"2\": 99, \"3\": 100, \"4\": 100, \"5\": 59, \"6\": 100, \"7\": 100}, \"pop\": {\"0\": 1.0, \"1\": 0.65, \"2\": 0.98, \"3\": 0.86, \"4\": 1.0, \"5\": 0.62, \"6\": 0.93, \"7\": 0.95}, \"prcp\": {\"0\": 40.0, \"1\": 1.65, \"2\": 14.01, \"3\": 5.07, \"4\": 16.55, \"5\": 2.17, \"6\": 2.77, \"7\": 1.73}, \"uvi\": {\"0\": 10.14, \"1\": 12.78, \"2\": 12.73, \"3\": 8.44, \"4\": 0.59, \"5\": 1.0, \"6\": 1.0, \"7\": 1.0}, \"temp.day\": {\"0\": 26.62, \"1\": 30.95, \"2\": 30.17, \"3\": 28.37, \"4\": 27.22, \"5\": 29.78, \"6\": 26.83, \"7\": 26.36}, \"tmpMin\": {\"0\": 25.64, \"1\": 24.64, \"2\": 25.84, \"3\": 25.56, \"4\": 25.72, \"5\": 24.86, \"6\": 25.96, \"7\": 25.47}, \"tmpMax\": {\"0\": 27.16, \"1\": 31.1, \"2\": 30.2, \"3\": 29.5, \"4\": 28.87, \"5\": 29.78, \"6\": 28.96, \"7\": 28.25}, \"temp.night\": {\"0\": 25.67, \"1\": 27.39, \"2\": 26.24, \"3\": 27.2, \"4\": 25.92, \"5\": 27.14, \"6\": 26.56, \"7\": 25.66}, \"temp.eve\": {\"0\": 25.91, \"1\": 28.73, \"2\": 27.42, \"3\": 28.27, \"4\": 27.94, \"5\": 29.29, \"6\": 28.96, \"7\": 28.12}, \"temp.morn\": {\"0\": 26.5, \"1\": 24.64, \"2\": 26.13, \"3\": 25.72, \"4\": 26.04, \"5\": 24.86, \"6\": 25.98, \"7\": 25.57}, \"feels_like.day\": {\"0\": 26.62, \"1\": 34.99, \"2\": 34.96, \"3\": 32.03, \"4\": 30.67, \"5\": 33.62, \"6\": 29.45, \"7\": 26.36}, \"feels_like.night\": {\"0\": 26.56, \"1\": 30.98, \"2\": 26.24, \"3\": 30.62, \"4\": 26.84, \"5\": 30.16, \"6\": 26.56, \"7\": 26.45}, \"feels_like.eve\": {\"0\": 26.85, \"1\": 32.49, \"2\": 30.94, \"3\": 31.8, \"4\": 31.51, \"5\": 33.17, \"6\": 32.64, \"7\": 31.18}, \"feels_like.morn\": {\"0\": 26.5, \"1\": 25.48, \"2\": 26.13, \"3\": 26.62, \"4\": 26.04, \"5\": 25.73, \"6\": 25.98, \"7\": 26.4}, \"date\": {\"0\": 1685098800000, \"1\": 1685185200000, \"2\": 1685271600000, \"3\": 1685358000000, \"4\": 1685444400000, \"5\": 1685530800000, \"6\": 1685617200000, \"7\": 1685703600000}, \"main\": {\"0\": \"Rain\", \"1\": \"Rain\", \"2\": \"Rain\", \"3\": \"Rain\", \"4\": \"Rain\", \"5\": \"Rain\", \"6\": \"Rain\", \"7\": \"Rain\"}, \"description\": {\"0\": \"lluvia moderada\", \"1\": \"lluvia ligera\", \"2\": \"lluvia moderada\", \"3\": \"lluvia ligera\", \"4\": \"lluvia moderada\", \"5\": \"lluvia ligera\", \"6\": \"lluvia ligera\", \"7\": \"lluvia ligera\"}, \"icono\": {\"0\": \"10d\", \"1\": \"10d\", \"2\": \"10d\", \"3\": \"10d\", \"4\": \"10d\", \"5\": \"10d\", \"6\": \"10d\", \"7\": \"10d\"}, \"alertPrecip\": {\"0\": \"X\", \"1\": \"-\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"alertAlertas\": {\"0\": \"-\", \"1\": \"-\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"alertVelViento\": {\"0\": \"-\", \"1\": \"-\", \"2\": \"X\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"alertTmpMax\": {\"0\": \"-\", \"1\": \"-\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"X\", \"6\": \"-\", \"7\": \"-\"}, \"alertTmpMin\": {\"0\": \"-\", \"1\": \"X\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"recomendaciones\": {\"lluvias\": \"Realice una revisi\\u00f3n y limpieza a la red de desague y canales existentes ENTER8 Cuente con una estaci\\u00f3n de bombeo, que debe estar ubicada en el punto m\\u00e1s bajo del predio. Aseg\\u00farese de encender y probar el sistema de bombeo al menos una vez al mes y hacer un mantenimiento mensual al equipo de bombeoENTER8 Los productos alojados en zonas de almacenamiento deben mantenersen sobre estibas - estanterias, con el fin de que no entren en contacto directo con el agua.\", \"vientos\": \"-\", \"temperatura\": \"-\"}}
'''

data = json.loads(jsonString)
pprint(data) #Pretty print

def alertAlertas(): # Para la primera alerta
  contador = 0 # Contar si hay alertas
  for k, v in data["alertAlertas"].items(): # Busca la primera
    if v == 'X': # Revisa si hay alerta
      print("Se presenta una alerta en alerAlertas en: " + str(v))
      for k_1, v_1 in data.items():
        if k_1 == "dt": # Para el tiempo
          for k_2, v_2 in v_1.items():
            if k == k_2:
              time = v_2
              fecha_utc = datetime.utcfromtimestamp(time).replace(tzinfo=timezone.utc) #Formula del tiempo
              local =  fecha_utc.astimezone() 
              print("El suceso tendra fecha y hora: " +str(local))
      contador += 1
  if contador == 0:
    print("No hay ninguna alerta en alertAlertas \n") # Si no hay alerta

def alertPrecip(): # Para la segunda alerta
  contador = 0 # Contar si hay alertas
  for k, v in data["alertPrecip"].items(): # Busca la primera
    if v == 'X': # Revisa si hay alerta
      contador += 1
      print("Se presenta una alerta en alerPrecip en: " + str(v))
      for k_1, v_1 in data.items():
        if k_1 == "dt": # Para el tiempo
          for k_2, v_2 in v_1.items():
            if k == k_2:
              time = v_2
              fecha_utc = datetime.utcfromtimestamp(time).replace(tzinfo=timezone.utc) #Formula del tiempo
              local =  fecha_utc.astimezone()
              print("El suceso tendra fecha y hora: " +str(local))
      for k_3, v_3 in data.items():
        if k_3 == "clouds": # nubes
          for k_4, v_4 in v_3.items():
            if k == k_4:
              print("Nivel de nubes: " +str(v_4))
      for k_5, v_5 in data.items():
        if k_5 == "humidity": # humedad
          for k_6, v_6 in v_5.items():
            if k == k_6:
              print("Nivel de humedad: " +str(v_6))
      for k_7, v_7 in data.items():
        if k_7 == "weather": # clima
          for k_8, v_8 in v_7.items():
            if k == k_8:
              print("Descripción del clima: " +str(v_8))
      for k_9, v_9 in data.items():
        if k_9 == "wind_gust": # rafaga de vientos
          for k_10, v_10 in v_9.items():
            if k == k_10:
              print("Rafaga de viento: " +str(v_10))
      for k_11, v_11 in data.items():
        if k_11 == "prcp": # precipitación
          for k_12, v_12 in v_11.items():
            if k == k_12:
              print("Nivel de precipiración: " +str(v_12))
      for k_13, v_13 in data.items():
        if k_13 == "pop": # Pop
          for k_14, v_14 in v_13.items():
            if k == k_14:
              print("Probabilidad estadística de que un punto dado en un área para la cual se está pronosticando, reciba al menos 0,01 mm de precipitación: " +str(v_14))
      for k_15, v_15 in data.items():
        if k_15 == "dew_point": # Punto de rocio
          for k_16, v_16 in v_15.items():
            if k == k_16:
              print("Punto de rocio: " +str(v_12))
      print("\n")
  if contador == 0:
    print("No hay ninguna alerta en alertPrecip \n") # Si no hay alerta

def alertTmpMax(): # Para la tercera alerta
  contador = 0 # Contar si hay alertas
  for k, v in data["alertTmpMax"].items(): # Busca la primera
    if v == 'X': # Revisa si hay alerta
      contador += 1
      print("Se presenta una alerta en alerTmpMax en: " + str(v))
      for k_1, v_1 in data.items():
        if k_1 == "dt": # Para el tiempo
          for k_2, v_2 in v_1.items():
            if k == k_2:
              time = v_2
              fecha_utc = datetime.utcfromtimestamp(time).replace(tzinfo=timezone.utc) #Formula del tiempo
              local =  fecha_utc.astimezone()
              print("El suceso tendra fecha y hora: " +str(local))
      for k_3, v_3 in data.items():
        if k_3 == "feels_like.day": # Sensación dia
          for k_4, v_4 in v_3.items():
            if k == k_4:
              print("La sensación termica en el dia: " +str(v_4))
      for k_5, v_5 in data.items():
        if k_5 == "feels_like.eve": # Sensación tarde
          for k_6, v_6 in v_5.items():
            if k == k_6:
              print("La sensación termica en la tarde: " +str(v_6))
      for k_7, v_7 in data.items():
        if k_7 == "feels_like.morn": # Sensación mañana
          for k_8, v_8 in v_7.items():
            if k == k_8:
              print("La sensación termica en la mañana: " +str(v_8))
      for k_9, v_9 in data.items():
        if k_9 == "feels_like.night": # Sensación noche
          for k_10, v_10 in v_9.items():
            if k == k_10:
              print("La sensación termica en la noche: " +str(v_10))
      for k_11, v_11 in data.items():
        if k_11 == "temp.day": # Temperatura dia
          for k_12, v_12 in v_11.items():
            if k == k_12:
              print("Temperatura del dia sera: " +str(v_12))
      for k_13, v_13 in data.items():
        if k_13 == "temp.eve": # Temperatura tarde
          for k_14, v_14 in v_13.items():
            if k == k_14:
              print("Temperatura de la tarde sera: " +str(v_14))
      for k_15, v_15 in data.items():
        if k_15 == "temp.morn": # Temperatura mañana
          for k_16, v_16 in v_15.items():
            if k == k_16:
              print("Temperatura de la madrugada sera: " +str(v_12))
      for k_17, v_17 in data.items():
        if k_17 == "temp.night": # Temperatura noche
          for k_18, v_18 in v_17.items():
            if k == k_18:
              print("Temperatura de la noche sera: " +str(v_18))
      for k_19, v_19 in data.items():
        if k_19 == "tmpMax": # Temperatura maxima
          for k_20, v_20 in v_19.items():
            if k == k_20:
              print("La temperatura maxima sera: " +str(v_20))
      for k_21, v_21 in data.items():
        if k_21 == "tmpMin": # Temperatura minima
          for k_22, v_22 in v_21.items():
            if k == k_22:
              print("La temperatura minima sera: " +str(v_22))
      print("\n")
  if contador == 0:
    print("No hay ninguna alerta en alertTempMax \n") # Si no hay alerta

def alertTmpMin(): # Para la cuarta alerta
  contador = 0 # Contar si hay alertas
  for k, v in data["alertTmpMin"].items(): # Busca la primera
    if v == 'X': # Revisa si hay alerta
      contador += 1
      print("Se presenta una alerta en alerTmpMax en: " + str(v))
      for k_1, v_1 in data.items():
        if k_1 == "dt": # Para el tiempo
          for k_2, v_2 in v_1.items():
            if k == k_2:
              time = v_2
              fecha_utc = datetime.utcfromtimestamp(time).replace(tzinfo=timezone.utc) #Formula del tiempo
              local =  fecha_utc.astimezone()
              print("El suceso tendra fecha y hora: " +str(local))
      for k_3, v_3 in data.items():
        if k_3 == "feels_like.day": # Sensación dia
          for k_4, v_4 in v_3.items():
            if k == k_4:
              print("La sensación termica en el dia: " +str(v_4))
      for k_5, v_5 in data.items():
        if k_5 == "feels_like.eve": # Sensación tarde
          for k_6, v_6 in v_5.items():
            if k == k_6:
              print("La sensación termica en la tarde: " +str(v_6))
      for k_7, v_7 in data.items():
        if k_7 == "feels_like.morn": # Sensación mañana
          for k_8, v_8 in v_7.items():
            if k == k_8:
              print("La sensación termica en la mañana: " +str(v_8))
      for k_9, v_9 in data.items():
        if k_9 == "feels_like.night": # Sensación noche
          for k_10, v_10 in v_9.items():
            if k == k_10:
              print("La sensación termica en la noche: " +str(v_10))
      for k_11, v_11 in data.items():
        if k_11 == "temp.day": # Temperatura dia
          for k_12, v_12 in v_11.items():
            if k == k_12:
              print("Temperatura del dia sera: " +str(v_12))
      for k_13, v_13 in data.items():
        if k_13 == "temp.eve": # Temperatura tarde
          for k_14, v_14 in v_13.items():
            if k == k_14:
              print("Temperatura de la tarde sera: " +str(v_14))
      for k_15, v_15 in data.items():
        if k_15 == "temp.morn": # Temperatura mañana
          for k_16, v_16 in v_15.items():
            if k == k_16:
              print("Temperatura de la madrugada sera: " +str(v_12))
      for k_17, v_17 in data.items():
        if k_17 == "temp.night": # Temperatura noche
          for k_18, v_18 in v_17.items():
            if k == k_18:
              print("Temperatura de la noche sera: " +str(v_18))
      for k_19, v_19 in data.items():
        if k_19 == "tmpMax": # Temperatura maxima
          for k_20, v_20 in v_19.items():
            if k == k_20:
              print("La temperatura maxima sera: " +str(v_20))
      for k_21, v_21 in data.items():
        if k_21 == "tmpMin": # Temperatura minima
          for k_22, v_22 in v_21.items():
            if k == k_22:
              print("La temperatura minima sera: " +str(v_22))
      print("\n")
  if contador == 0:
    print("No hay ninguna alerta en alertTempMax \n") # Si no hay alerta

def alertVelViento(): # Para la quinta alerta
  contador = 0 # Contar si hay alertas
  for k, v in data["alertVelViento"].items(): # Busca la primera
    if v == 'X': # Revisa si hay alerta
      contador += 1
      print("Se presenta una alerta en alerViento en: " + str(v))
      for k_1, v_1 in data.items():
        if k_1 == "dt": # Para el tiempo
          for k_2, v_2 in v_1.items():
            if k == k_2:
              time = v_2
              fecha_utc = datetime.utcfromtimestamp(time).replace(tzinfo=timezone.utc) #Formula del tiempo
              local =  fecha_utc.astimezone()
              print("El suceso tendra fecha y hora: " +str(local))
      for k_3, v_3 in data.items():
        if k_3 == "velViento": # Velocidad viento
          for k_4, v_4 in v_3.items():
            if k == k_4:
              print("La velocidad del viento: " +str(v_4))
      for k_5, v_5 in data.items():
        if k_5 == "pressure": # Presión
          for k_6, v_6 in v_5.items():
            if k == k_6:
              print("La presión de ese dia sera: " +str(v_6))
      for k_7, v_7 in data.items():
        if k_7 == "dirViento": # Dirección de viento
          for k_8, v_8 in v_7.items():
            if k == k_8:
              print("La dirección del viento: " +str(v_8))
      print("\n")
  if contador == 0:
    print("No hay ninguna alerta en alertTempMax \n") # Si no hay alerta

alert_1 = alertAlertas()
alert_2 = alertPrecip()
alert_3 = alertTmpMax()
alert_4 = alertTmpMin()
alert_5 = alertVelViento()
```


### Punto 5

Para este punto lo que hacemos es utilizar los codigos que nos eneseño el profe felipe, en el que usamos requests, para sacar el json, el usuario ingresa el nombre que desee y el codigo le devuelve la edad probable, la probabilidad de su genero, y de que pais puede ser. 
```
import json #Importamos json
import requests # Requests
from pprint import pprint # Prety print

url = 'https://api.agify.io?name=' # Link de edad
url_1 = 'https://api.genderize.io?name=' # Link de genero
url_2 = 'https://api.nationalize.io?name=' # Link de nacionalidad

def predecir_edad(num : str): # Función que predice la edad
  peticion = requests.get(url+str(num)) # Busca en la web
  return json.loads(peticion.content) # Devuelve el json

def predecir_genero(num : str): # Función que predice genero
  peticion = requests.get(url_1+str(num)) # Busca en la web
  return json.loads(peticion.content) # Devuelve el json

def predecir_nacionalidad(num : str): # Función que predice genero
  peticion = requests.get(url_2+str(num)) # Busca en la web
  return json.loads(peticion.content) # Devuelve el json

def dic_unido(dic_1, dic_2, dic_3): # Función que une los diccionarios
  diccionario_nombre = {} #Diccionario vacio
  diccionario_nombre.update(dic_1) #Diccionario edad
  diccionario_nombre.update(dic_2) #Diccionario genero
  diccionario_nombre.update(dic_3) #Diccionario nacionalidad
  return diccionario_nombre

if __name__ == "__main__": 
  Name = input("Ingresa un nombre: ") # Ingresa nombre
  respuesta = predecir_edad(Name) # Ejecutar función 1
  respuesta_ = predecir_genero(Name) # Ejecutar función 2
  respuesta_1 = predecir_nacionalidad(Name) # Ejecutar función 3
  nom_dic = dic_unido(respuesta, respuesta_, respuesta_1) # Ejecutar función 4
  print(Name) # Nombre
  pprint(nom_dic) #Pretty print
```
