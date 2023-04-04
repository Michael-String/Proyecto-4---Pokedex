# Proyecto 4: Pokédex
# UCamper: Michel Amir Madrigal Torres
# Bootcamp: Fundamentos de Python
# Coach: Gustavo Mota
# Grupo: C5

import requests 
import matplotlib.pyplot as plt 
import matplotlib.image as img



pokemon = input ("¡Hola poketrainer, ingresa el nombre del pokemon que quieres ver!: ") 
url="https://pokeapi.co/api/v2/pokemon/" + pokemon
res= requests.get(url) 
if res.status_code != 200: 
    print("No encontramos a ese pokemon... :(") 
    exit()

     
imagen= img.imread(res.json()['sprites']['front_default']) 
plt.title(res.json()['name'])
imgplot = plt.imshow(imagen)
plt.show()



   