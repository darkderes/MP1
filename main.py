from collections import defaultdict

tipos_de_pokemon = set()
pokemon_por_tipo = dict()
info_pokemon = dict()

def def_value():
    return "No es una opción"

## Definición funciones ##

def orden_segun(tipo, criterio):
    pokemones = list()
    criterioData = []
    ListaDesordenada = []

    open_file = open("pokemon.csv", "r")
    for(linea, pokemon) in enumerate(open_file):
     if linea == 0:
        continue
     pokemon = pokemon.split(",")
     pokemon_tipos = pokemon[2].split(";")
     if(pokemon_tipos[0] == tipo)or(pokemon_tipos[1] == tipo):
         pokemones.append(pokemon[1])
         if(criterio == "HP"):        
            criterioData.append(int(pokemon[3]))
         elif(criterio == "Ataque"):
            criterioData.append(int(pokemon[4]))
         elif(criterio == "Defensa"):
            criterioData.append(int(pokemon[5]))
    for pokemonTemp in zip (pokemones, criterioData):
            ListaDesordenada.append(pokemonTemp)  
    # funcion lamba no estudiada en clases , pero investigada como objeto de estudio para el curso de python 
    listaOrdenada = sorted(ListaDesordenada, key=lambda x: x[1],reverse=True)
    # se ocupa tecnica de destructuracion para obtener los valores de nombre de pokemon y criterio, para la posterior retorno del nombre de pokemon ordenado
    (pokemonNombre,pokemonCriterio) = list(zip(*listaOrdenada))

    return(pokemonNombre)

def estadisticas(tipo, criterio):
    pokemones = list()
    HP = []
    ListaData = []
    open_file = open("pokemon.csv", "r")
    for(linea, pokemon) in enumerate(open_file):
     if linea == 0:
        continue
     pokemon = pokemon.split(",")
     pokemon_tipos = pokemon[2].split(";")
     if(pokemon_tipos[0] == tipo)or(pokemon_tipos[1] == tipo):
         pokemones.append(pokemon[1])
         if(criterio == "HP"):        
            HP.append(int(pokemon[3]))
         elif(criterio == "Ataque"):
            HP.append(int(pokemon[4]))
         elif(criterio == "Defensa"):
            HP.append(int(pokemon[5]))
    for pokemonTemp in zip (pokemones, HP):
            ListaData.append(pokemonTemp)  
    
    #lista2 = sorted(ListaOrdenada, key=lambda x: x[1],reverse=True)
    (pokemonNombre,pokemonCriterio) = list(zip(*ListaData))
    Dict_Poke = {'max':max(pokemonCriterio), 'min':min(pokemonCriterio), 'prom':sum(pokemonCriterio)/len(pokemonCriterio)}
    return(Dict_Poke)


def tipo_segun_nombre(nombre):
    tipo = list()
    open_file = open("pokemon.csv", "r")
    for(linea, pokemon) in enumerate(open_file):
     if linea == 0:
        continue
     pokemon = pokemon.split(",")
     if(pokemon[1] == nombre):
        pokemon_tipos = pokemon[2].split(";")
        tipo.append(pokemon_tipos[0]) 
        tipo.append(pokemon_tipos[1])
        break
    return(tuple(tipo))  
    
## Lectura archivo y definicion estructuras ##

pokemon_por_tipo = defaultdict(lambda: ([],[]), {})

open_file = open("pokemon.csv", "r")
for(linea, pokemon) in enumerate(open_file):
    if linea == 0:
        continue    
    pokemon = pokemon.split(",")
    pokemon_tipos = pokemon[2].split(";")

    # 1.1Codigo agrega elementos a un set para evitar elementos repetidos provenientes de la lista de pokemon_tipos , se entiende que el primer tipo quizas nunca sea vacio 
    # pero igual se hizo una validacion a modo de entendimiento del codigo
    if pokemon_tipos[0] != "" :     
      tipos_de_pokemon.add(pokemon_tipos[0])
    if pokemon_tipos[1] != "" :
      tipos_de_pokemon.add(pokemon_tipos[1])
     # 1.2 diccionario de datos de pokemon por tipo
    pokemon_por_tipo[pokemon_tipos[0]][0].append(pokemon[0])
    pokemon_por_tipo[pokemon_tipos[1]][1].append(pokemon[0])
     # 1.3 Codigo genera diccionario info_pokemon
    info_pokemon[pokemon[0]] = [pokemon[1],pokemon[3],pokemon[4],pokemon[5],pokemon[6].strip()] 

## Menu flujo principal ##

acciones = defaultdict(def_value)
acciones["1"] = "orden segun"
acciones["2"] = "estadisticas"
acciones["3"] = "encontrar tipo"
acciones["4"] = "revisar"
acciones["0"] = "salir"

continuar = True
while continuar:
    
    print('''
¿Que desea hacer?

1.- Ordenar segun criterio
2.- Obtener estadísticas
3.- Saber el tipo de un pokemon
4.- Revisar Estructuras
0.- Salir
    ''')

    accion = input()
    accion = acciones[accion]

    if accion == "orden segun":
        tipo = input()
        criterio = input()
    
        orden = orden_segun(tipo, criterio)

        print(f"Ordenando pokemon de tipo {tipo} segun {criterio}:")
        for elem in orden:
            print(f"  - {elem}")

    elif accion == "estadisticas":
        tipo = input()
        criterio = input()

        datos = estadisticas(tipo, criterio)

        print(f"Informacion de {criterio} en pokemon de tipo {tipo}")
        print(f"  - Máximo: {datos['max']}")
        print(f"  - Mínimo: {datos['min']}")
        print(f"  - Promedio: {round(datos['prom'],1)}")

    elif accion == "encontrar tipo":

        nombre = input()

        tipos = tipo_segun_nombre(nombre)

        print(f"El tipo principal de {nombre} es {tipos[0]}")

        if tipos[1] == "":
            print(f"{nombre} no tiene tipo secundario")
        else:
            print(f"El tipo secundario de {nombre} es {tipos[1]}")

    elif accion == "revisar":
        try:
            print("Tipos Encontrados:")
            for tipo in sorted(list(tipos_de_pokemon)):
                print(f"  - {tipo}")

            print("")
   
            p = pokemon_por_tipo["Electric"]
            print(f"Revisando Primarios: {'25' in p[0]}")
            print(f"Revisando Secundarios: {'170' in p[1]}")
            print("")
            print("Pokemon Ejemplo:")
            i = info_pokemon["25"]
            esta = "Electric" in i
            print(f"  - Nombre: {i[0]}")
            print(f"  - Esta Tipo: {esta}")
        except NameError:
            print("Esta parte no se puede ejecutar ya que aún no has definido todas las estructuras")
            
    elif accion == "salir":
        continuar = False
    else:
        print(accion)