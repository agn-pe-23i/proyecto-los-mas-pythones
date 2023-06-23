import json
from menu import continuar

def cargar_catalogo():
    nombre_archivo = input("Ingrese el nombre del archivo de catálogo a cargar (sin extension .json): ")
    try:
        with open(nombre_archivo + '.json', "r", encoding='utf-8') as archivo:
            catalogo = json.load(archivo)
        print("\nCatálogo cargado correctamente.")
        continuar()
        return catalogo
    except FileNotFoundError:
        print("\nEl archivo especificado no existe.")
        continuar()
        return
    except json.JSONDecodeError:
        print("\nEl archivo de catálogo no está en un formato válido.")
        continuar()
        return
    return None

def guardar_catalogo(catalogo):
    if catalogo is None:
        print('No existe un catálogo para guardar.')
        continuar()
        return
    else:
        nombre_archivo = input("Ingrese el nombre del archivo donde se guardará el catálogo: ")
        try:
            with open(nombre_archivo + '.json', "w", encoding='utf-8') as archivo:
                json.dump(catalogo, archivo)
            print("\nCatálogo guardado correctamente.")
            continuar()
            return
        except:
            print("\nNo se pudo guardar el catálogo. Verifique el nombre del archivo y los permisos de escritura.")
            continuar()
            return