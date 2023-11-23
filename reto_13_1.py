# -*- coding: utf-8 -*-
"""Reto_13_1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GUnfyQypiFKMAAOt9GXQWZdpzzelA_po
"""

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