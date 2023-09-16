# -*- coding: utf-8 -*-
"""JuegoDeCartas.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SyNbBnoM-0n_Un85GXSorNmXq1xX__OS
"""

import random #Importamos random
class Carta(object):  #Definimos la clase carta
  #Constructor de la clase carta
  def __init__(self, palo, valor):
    self.palo = palo
    self.valor = valor
  #Método Imprimir
  def imprimir(self):
    print("{} de {}".format(self.valor, self.palo))


class Mazo(object):  #Definimos la clase mazo
  #Constructor de la clase mazo
  def __init__(self):
    self.cartas=[]
    self.mazo()
  def mazo(self):
    for s in ["Corazones", "Diamantes" , "Tréboles","Picas"]:
      for v in range(1,14):
         self.cartas.append(Carta(s,v))
  #Método para mostrar el mazo
  def mostrar_mazo(self):
    for c in self.cartas:
      c.imprimir()
  #Método para mezclar el mazo
  def mezclar(self):
    for i in range(len(self.cartas)-1,0,-1):
      r = random.randint(0,i)
      self.cartas[i],self.cartas[r]=self.cartas[r],self.cartas[i]
  #Método para robar una carta
  def robar(self):
    return self.cartas.pop()


class Jugador(object): #Definimos la clase jugador
  #Constructor de la clase jugador
  def __init__(self,nombre):
    self.mano = []  
    self.nombre=nombre
  #Método para robar una carta de un mazo
  def robar(self,mazo):
    self.mano.append(mazo.robar())
  #Método para mostrar su mano
  def mostrar_mano(self):
    for carta in self.mano:
      carta.imprimir()

baraja=Mazo()
Max=Jugador("Max")
for i in range(5):
  Max.robar(baraja)
Max.mostrar_mano()