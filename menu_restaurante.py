menu = {
    1: {
        "nom": "Pasta rica",
        "ingredientes": {
            "pasta (g)": 100,
            "salsa (ml)": 150,
            "queso parmesano(g)": 30,
            "sal (g)": 2
        }
    },
    2: {
        "nom": "Ensalada Fresquita",
        "ingredientes": {
            "lechuga (g)": 40,
            "tomate (g)": 60,
            "Aceite (ml)": 5,
            "Sal (g)":1
        }
    },
    3: {
        "nom": "Sopa de verduritas",
        "ingredientes": {
            "agua (ml)": 350,
            "Zanahoria (g)": 150,
            "papa (g)": 80,
            "cebolla (g)": 30,
            "apio (g)": 30,
            "aceite (ml)": 5,
            "cilantro (g)": 5,
            "calabacin (g)": 50,
            "sal (g)": 2
        }
    },
    4:  {
        "nom":"Tacos de queso mexicanos",
        "ingredientes":{
            "tortillas de maiz (Unidades)":2,
            "Queso rallado (g)":50,
            "Mantequilla o aceite (g)": 5
        }
        
    },
    5: {
        "nom": "Pechuga de pollo a la plancha",
        "ingredientes":{
            "Pechiga de pollo (g)":150,
            "Sal (g)":2,
            "Pimienta (g)": 0.5,
            "Aceite para cocinar (ml)":5   
        }
    }
}

print("==== MENU RESTAURANTE DE RICARDO ====")
for opcion, datos in menu.items():
    print(f"{opcion}. {datos['nom']}")
    
opcion = int(input("Selecciona una opcion del menu: "))

if opcion not in menu:
    print("Esta opcion no esta en el menu :(( ))")
else:
    cantidad = int(input("Digita la cantidad de platos: "))

    plato = menu[opcion]
    print(f"\nEstos son los Ingredientes necesarios para {cantidad} porciones de {plato['nom']}:\n :D")


    ingredientes = plato["ingredientes"]


    for item, cantidad_base in ingredientes.items():
        total = cantidad_base * cantidad
        print(f"{item}: {total}")