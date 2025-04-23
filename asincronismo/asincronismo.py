"""
Ejemplo de asincronismo
"""
import asyncio
import httpx
import time

async def imprimir_mensajes():
    print("Acá sigo con el programa")
    await asyncio.sleep(4)
    print('ultima linea del codigo')

async def obtener_clima(ciudad):
    url = f"https://wttr.in/{ciudad}?format=3"
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, timeout=5.0)
            print(response.text)
        except httpx.RequestError as e:
            print(f"Error al consultar {ciudad}: {e}")

async def main():
    ciudades = ["Buenos Aires", "Córdoba", "Rosario", "Mendoza", "Salta"]
    tareas = [obtener_clima(ciudad) for ciudad in ciudades]
    await asyncio.gather(*tareas)


async def wrapper():
    await asyncio.gather(
        imprimir_mensajes(),
        main()
        
    )

if __name__ == "__main__":
    asyncio.run(wrapper())
