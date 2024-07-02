total = 0
total_cosas = 0
total_calorias = 0

def guardarCarrito(nombre_usuario: str, carrito: list[dict]) -> None:
    nombre_archivo = f"{nombre_usuario}.txt"

    with open(nombre_archivo, 'w',encoding='utf-8') as archivo:
        global total_cosas,total,total_calorias
        archivo.write(f"Carrito de {nombre_usuario}\n")
        archivo.write("-" * 20 + "\n")

        for item in carrito:
            archivo.write(f"Comida: {item['comida']}\n")
            archivo.write(f"Precio: ${item['precio']}\n")
            archivo.write("-" * 20 + "\n")

        archivo.write(f"Total Items: {total_cosas}\n")
        archivo.write(f"Total $ {total}\n")
        archivo.write(f"Total Calorías: {total_calorias} Kcal\n")
        archivo.write(f"Gracias, vuelva prontos 💁🏿‍♂️🛍️👋")


    print(f"Carrito guardado en {nombre_archivo}")



def selecItemList (lista:list, nombreLista:str) -> int:
    print('--',nombreLista,'--')
    for i, item in enumerate(lista):
        print(i+1, item)

    while (True):
        selec = int(input('>> '))-1
        if (selec in range(len(lista))):
            return selec

def filtrarCarrito (lista:list[dict], llave:str, filtro:str) -> list[dict]:
    lista_filtrada = []
    for elemento in lista:
        if (str(elemento[llave]) == str(filtro)):
            lista_filtrada.append(elemento)
    return lista_filtrada

def eliminaItem(carrito:list) -> None:
    print('--', 'Eliminar de carrito', '--')
    global total, total_cosas, total_calorias
    for num, platillos in enumerate(carrito):
        print(num+1, platillos)
    seleccion = input(">> ")
    eliminado = carrito.pop(int(seleccion)-1)
    total_calorias -= eliminado['kcal']
    total -= eliminado['precio']
    print("TOTAL $",total)
    total_cosas -= 1
    print("ITEMS ",total_cosas)
    

def verDeuda(total:int, total_cosas:int) -> bool:
    propina = total * 0.10
    deuda = total + propina
    print('--','Total a pagar','--')
    print("La cantidad de items son:", total_cosas)
    print("El precio a pagar es de: $", total)
    print("La propina sugerida es de: $", propina)
    print("¿Desea pagar $", deuda, "?")
    while True:
        elegir = int(input("(1.Pagar)(2.Seguir comprando) >>"))
        if elegir == 1:
            print("Compra completada")
            return True
        if elegir == 2:
            return False

def verCarrito(carrito:list, nombreCarrito:str='Carrito') -> None:
    print('--', nombreCarrito, '--')
    global total_calorias, total,total_cosas
    for cosas, item in enumerate(carrito):
        print(cosas+1, item)
    print("\nTotal items: ",total_cosas)
    print("Total $",total)
    print("Total Calorias -> ", total_calorias,"\n")

def imprimirListaCarta(lista:list[dict], nombreLista:str='Lista') -> None:
    print('--', nombreLista, '--')
    for i, plato in enumerate(lista):
        print(i+1, plato['comida'], "$", plato['precio'])
    print('-'*10)        

def selecOpcMenu(menu:dict, nombreMenu:str='Menu') -> int:
    print('\n--', nombreMenu, '--')
    for opcion in menu.keys():
        print(menu[opcion], opcion)

    while True:
        selec = int(input('>> '))
        if selec in menu.values():
            return selec

carta = [
    {'comida': 'papas fritas', 'precio': 2000, 'kcal': 2000, 'ingredientes': 'papas,aceite'},
    {'comida': 'completo', 'precio': 2500, 'kcal': 3000, 'ingredientes': 'vienesa,pan,palta,tomate'},
    {'comida': 'churrasco chacarero', 'precio': 2700, 'kcal': 3260, 'ingredientes': 'carne,pan,palta,porotos verdes'},
    {'comida': 'espagueti', 'precio': 1500, 'kcal': 1760, 'ingredientes': 'fideos,salsa,carne'}
]

opcionesMenu = {
    'salir': 0,
    'mostrar carta': 1,
    'seleccionar comida': 2,
    'ver carrito': 3, 
    'pagar': 4, 
    'quitar': 5, 
    'buscar filtro': 6, #falta filtro de alergias
    'buscar': 7, #falta esto, no se que es
    'modificar': 8,
    'agregar': 9, #en proceso
    'guardar carrito': 10, #falta esto
    'cargar carrito': 11, #falta esto

}

carrito = []
alergias = []

usuario = str(input("Ingrese usuario >>")).lower()
contraseña = input("Ingrese su contraseña >>")
alergias.append(input("Escriba sus alergias >>"))

while True:
    sel_opcion = selecOpcMenu(opcionesMenu)

    if sel_opcion == opcionesMenu['salir']:
        break

    if sel_opcion == opcionesMenu['mostrar carta']:
        print('--', "Carta", '--')
        for i, indice in enumerate(carta):
            print(i+1, "=>", indice['comida'], "$", indice['precio'], "|| ","Kcal:", indice['kcal'], "/ ", "Ingredientes:", indice['ingredientes'])
        print('-'*10)

    if sel_opcion == opcionesMenu['seleccionar comida']:
        imprimirListaCarta(carta, 'Platos')

        sel = int(input(">> ")) - 1
        platoselec = carta[sel]
        for key in platoselec:
            print(key, '=>', platoselec[key])
        carrito.append(platoselec)
        total += platoselec['precio']
        total_cosas += 1
        total_calorias += platoselec['kcal']
    
    if sel_opcion == opcionesMenu['ver carrito']:
        verCarrito(carrito, 'Items')

    if sel_opcion == opcionesMenu['pagar']:
        if verDeuda(total, total_cosas):
            carrito.clear()
            total = 0
            total_cosas = 0
    
    if sel_opcion == opcionesMenu['quitar']:
        eliminaItem(carrito)

    if (sel_opcion == opcionesMenu['buscar filtro']):
        lista_filtros = ['comida', 'ingredientes']
        sel_filtro = selecItemList(lista_filtros,'Tipo de filtro')
        lista_filtrada = filtrarCarrito(
            carrito,
            lista_filtros[sel_filtro],
            input('ingrese filtro: ')
        )
        imprimirListaCarta(lista_filtrada,'Resultado Filtro')

    if contraseña == "abcd12345" and (sel_opcion == opcionesMenu['modificar']):
        
        comida_selec = carta[selecItemList(carta,'Seleccionar')]
        print("Seleccione plato a modificar")
        lista_llaves = list(comida_selec.keys())
        llave_mod = lista_llaves[selecItemList(lista_llaves,'Llaves a Modificar')]
        print('Modificar:')
        comida_selec[llave_mod] = input('>> ')
    
    if sel_opcion == opcionesMenu['guardar carrito']:
        guardarCarrito(usuario,carrito)
    



