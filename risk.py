import random as ran

def numeroDado():
  #Esta función me genera un numero aleatorio entre 0 y 1
  lanzamiento = ran.random()
  #Se comprueba usando la función acumulada qué número del dado se obtiene
  if lanzamiento <= 1/6:
    resultado = 1
  elif lanzamiento <= 2/6:
    resultado = 2
  elif lanzamiento <= 3/6:
    resultado = 3
  elif lanzamiento <= 4/6:
    resultado = 4
  elif lanzamiento <= 5/6:
    resultado = 5
  elif lanzamiento <= 1:
    resultado = 6

  #Se retorna el resultado del lanzamiento del dado
  return resultado

#funcion atacante
def resultadosAtacante():
  #Lista donde se almacenarán los 3 resultados de los atacantes
  atacanteResu = []
  #Variable iteradora
  i = 0
  while i < 3:
    #Por cada iteración se agrega el resultado de la función numeroDado dentro de la lista atacanteResu
    atacanteResu.append(numeroDado())
    #Se actualiza la variable iteradora
    i += 1
  #Se organiza de mayor a menor la lista que contiene los resultados de los dados de los atacantes
  atacanteResu.sort(reverse=True)
  #Retornamos la lista obtenida
  return atacanteResu


#funcion defensa
def resultadosDefensa():
  #Lista donde se almacenarán los 2 resultados de los defensores
  defensaResu = []
  #Variable iteradora
  i = 0
  while i < 2:
    #Por cada iteración se agrega el resultado de la función numeroDado dentro de la lista defensaResu
    defensaResu.append(numeroDado())
    #Se actualiza la variable iteradora
    i += 1
  #Se organiza de mayor a menor la lista que contiene los resultados de los dados de los defensores
  defensaResu.sort(reverse=True)
  #Retornamos la lista obtenida
  return defensaResu


#Funcion para analizar los resultados de la batalla
def batalla():
  #Victorias por soldado de cada bando en una batalla 
  ganaAtq = 0
  ganaDef = 0
  #Se obtienen las listas de los resultados de cada lanzamiento de dado por bando
  a = resultadosAtacante()
  b = resultadosDefensa()
  #Variable iteradora
  i = 0
  while i < 2:
    #Comparamos los elementos de ambas listas
    #En este caso, b[i] que representa a los defensores es mayor o igual al a[i] que representa a los atacantes, se le de un punto a ganaDef
    if b[i] >= a[i]:
      ganaDef += 1 
    #En caso contrario quiere decir que a[i] será estrictamente mayor a b[i] y se le dará un punto a ganaAtq
    else:
      ganaAtq += 1
    #Se actualiza la variable iteradora
    i +=1

  #Con estos condicionales se busca saber quién ganó la batalla
  #En caso de haber empate de puntos o que los puntos de ganaAtq sean menores a los de ganaDef se retornará 0 (Dato que se usará después)
  if (ganaDef == ganaAtq) or (ganaAtq < ganaDef):
    return 0
  #En caso contrario, el puntaje ganaAtq es estrictamente mayor a ganaDef se retornará 1 (Dato que se usará después)
  else:
    return 1 #ganó atacante


#Input para las cantidades de pruebas
e = input("Escribe el número de escenarios: ")
escenas = int(e)
iteraciones = 0
#Variable que contabilizará las victorias del bando de los atacantes
ganaAtaq = 0

#Ciclo para hacer todas las batallas que se solicitaron
while iteraciones < escenas:
  #Resul tendrá 2 posibilidades (1 si los atacantes ganan / 0 si los defensores ganan) valroes obtenidos de la función batalla()
  resul = batalla()
  #Si resul es igual a 1 (Victoria de los atacantes), se actualiza la varibale ganaAtaq
  if resul == 1:
    ganaAtaq += 1
  #Se actualiza la variable iteradora
  iteraciones +=1

#Prints mostrando la información pertinente de las proporciones de victorias
print("La proporción de victorias del bando de los atacantes es de: ", ganaAtaq/escenas)
print("La proporción de victorias del bando de los defensores es de: ", 1-(ganaAtaq/escenas))




