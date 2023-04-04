import requests
import json
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#Definimos la URL para llamar a la API
endpoint = 'pokemon'
url= f"https://pokeapi.co/api/v2/pokemon{endpoint}/"

#Conseguimos la lista disponible de los pokemon:

response = requests.get(url)
data = response.json()

numero_pokemones = data ["count"]

url2 = f'{url}?Limit={numero_pokemones}&offset=0'

response2 = requests.get(url2)
data2 = response2.json()

Lista_de_pokemones = data2["results"]
print (Lista_de_pokemones)
Lista_de_nombres = [ pokemon["name"] for pokemon in Lista_de_pokemones ] 

#Conseguimos los datos de algun Pokemon:

pokemon_seleccionado = input("Selecciona un Pokemon: ")

if pokemon_seleccionado in Lista_de_nombres:
   print('Buscando Pokemon...')
   # Si existe, que muestre una imagen y las estadísticas (peso, tamaño, movimientos, habilidades y tipos)
   url3 = f'{url}/{pokemon_seleccionado}'
   response3 = requests.get(url3)
   
   data3 = response3.json()
   
   # Peso
   peso =  data3["weight"]
   print(f'El peso de{pokemon_seleccionado}es{peso}kg')
   
   # Tamaño
   tamaño = data3["height"]
   print(f'El tamaño de{pokemon_seleccionado}es{tamaño}cm')
   
   # Movimientos
   movimientos = data3["moves"]
   Lista_de_movimientos = [movimiento["move"]["name"] for movimiento in movimientos]
  
   print(f'Los movimientos de {pokemon_seleccionado}es: {Lista_de_movimientos}')
   
   # Habilidades
   habilidades = data3["abilities"]
   Lista_de_habilidades = [ habilidad["ability"]["name"]for habilidad in habilidades]
   print(f'Las habilidades de {pokemon_seleccionado} son {Lista_de_habilidades}')
   
    # Tipos
   tipos = data3["types"]
   lista_de_tipos = [ tipo["type"]["name"]for tipo in tipos]
   print(f'Los tipos de {pokemon_seleccionado} son {lista_de_tipos}')
   
   # Muestra la imagen
   imagen = data3["sprites"]["front_default"]
   plt.imshow(mpimg.imread(imagen))
   plt.show()

   # Registrando datos del Pokemon en json
 
   f_name = f'pokedex/{pokemon_seleccionado}.json'

   with open(f_name, 'w') as file:
     json.dump(data3, file, indent=4)
     
else:
   print("No hay registros de ese Pokemon")
   exit()



