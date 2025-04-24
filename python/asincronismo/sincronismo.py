"""
Ejemplo de sincronismo
"""
import requests, time

def imprimir_mensajes():
    print("Espero 4 segundos bloqueantes...")
    time.sleep(4)
    print('Termino la espera de 4 segundos.')


def obtener_clima(ciudad):
    url = f"https://wttr.in/{ciudad}?format=3"
    try:
        response = requests.get(url, timeout=5.0)
        print(response.text)
    except requests.RequestException as e:
        print(f"Error al consultar {ciudad}: {e}")

def main():
    ciudades = ["Buenos Aires", "Córdoba", "Rosario", "Mendoza", "Salta"]
    for ciudad in ciudades:
        obtener_clima(ciudad)

if __name__ == "__main__":
    imprimir_mensajes()
    main()