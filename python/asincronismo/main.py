"""
Para hacer una prueba con asincronismo hago un programa que envie un email a modo de
notificación al mismo tiempo que consume datos de dos apis distintas
"""
from email.message import EmailMessage
import aiosmtplib
import requests
import smtplib
import time
import asyncio
import httpx
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#para este ejemplo use mailtrap https://mailtrap.io/
EMAIL_USER = ''
EMAIL_PASSWORD = ''
"""
BLOQUE DE SINCRONISMO
"""
def envio_email_sinc(emails:list[str]):

    for email in emails:
        mensaje = MIMEMultipart()
        mensaje['From'] = 'server@example.com'
        mensaje['To'] = email
        mensaje['Subject'] = 'Probando Asincronismo'

        cuerpo = f'El usuario con email {email} hizo la siguiente consulta'
        mensaje.attach(MIMEText(cuerpo, 'plain'))

        with smtplib.SMTP('sandbox.smtp.mailtrap.io', 587) as servidor:
            servidor.login(EMAIL_USER, EMAIL_PASSWORD)
            servidor.send_message(mensaje)
            print("Correo enviado (simulado en Mailtrap)")


def consulto_direccion_sinc(lista_de_direcciones:list):
    for direccion in lista_de_direcciones:
        try:
            url = f"https://servicios.usig.buenosaires.gob.ar/normalizar/?direccion={direccion},%20caba"
            response = requests.get(url, timeout=8.0)
            print(response.text)
        except requests.RequestException as e:
            print(f"Error al consultar la direccion {direccion}: {e.__str__()}")
    
def ejecuto_funciones_sincronicas(emails:list[str], direcciones:list[str]):
    envio_email_sinc(emails)
    consulto_direccion_sinc(direcciones)

"""
FIN BLOQUE SINCRONISMO
"""


"""
BLOQUE DE ASINCRONISMO
"""
async def armo_envio_de_emails(email:str):
    mensaje = EmailMessage()
    mensaje["From"] = "server@example.com"
    mensaje["To"] = email
    mensaje["Subject"] = "Correo asincrónico"
    mensaje.set_content(f"Hola {email}, este es un correo enviado de forma asincrónica.")

    await aiosmtplib.send(
        mensaje,
        hostname="sandbox.smtp.mailtrap.io",
        port=587,
        start_tls=True,
        username=EMAIL_USER,
        password=EMAIL_PASSWORD
    )
    print(f"Correo enviado a {email}")


async def envio_de_emails_sync(emails:list[str]):
    emails = [ armo_envio_de_emails(email) for email in emails]
    await asyncio.gather(*emails)


async def obtengo_info_direccion(direccion:str):
    url = f"https://servicios.usig.buenosaires.gob.ar/normalizar/?direccion={direccion},%20caba"
    async with httpx.AsyncClient() as client:
        try:      
            response = await client.get(url, timeout=8.0)
            print(response.text)
        except httpx.RequestError as e:
            print(f"Error al consultar la direccion {direccion}: {e.__str__()}")


async def consulto_direccion_async(lista_de_direcciones:list):
    direcciones = [ obtengo_info_direccion(direccion) for direccion in lista_de_direcciones]
    await asyncio.gather(*direcciones)


async def ejecuto_funciones_asincronicas(emails:list[str], direcciones:list[str]):
    await asyncio.gather(
        consulto_direccion_async(direcciones),
        envio_de_emails_sync(emails)
    )
"""
FIN BLOQUE ASINCRONISMO
"""

if __name__ == "__main__":
    emails = ["christian@gmail.com", "zahira@gmail.com", "sasha@gmail.com"]
    direcciones = ["las tunas 11122", "lacarra 535", "rodo 5533"]

    # inicio contador
    inicio = time.time()

    #ejecuto_funciones_sincronicas(emails, direcciones)
    asyncio.run(ejecuto_funciones_asincronicas(emails, direcciones))

    # finalizo contador
    fin = time.time()

    # tiempo transcurrido
    duracion = fin - inicio
    print(f"El programa tardó {duracion:.2f} segundos en ejecutarse.")

"""
test de tiempos con sincronismo:
primera prueba: El programa tardó 8.49 segundos en ejecutarse.
segunda prueba: El programa tardó 9.66 segundos en ejecutarse.
tercera prueba: El programa tardó 21.81 segundos en ejecutarse.
cuarta prueba: El programa tardó 24.72 segundos en ejecutarse.
quinta prueba: El programa tardó 10.21 segundos en ejecutarse.

test de tiempos con asincronismo:
primera prueba: El programa tardó 4.99 segundos en ejecutarse.
segunda prueba: El programa tardó 7.32 segundos en ejecutarse.
tercera prueba: El programa tardó 12.02 segundos en ejecutarse.
cuarta prueba: El programa tardó 3.72 segundos en ejecutarse.
quinta prueba: El programa tardó 5.44 segundos en ejecutarse.

Conclusión:
si tengo que enviar muchos correos y consultar muchas veces apis externas
lo recomendable es hacerlo de forma asincrónica ya que como se puede ver
los tiempos empleados son menores
"""