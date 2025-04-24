from celery import shared_task
import time

@shared_task(bind=True)
def enviar_correo(self, email):
    try:
        print(f"Enviando correo a {email}")
        time.sleep(30)
        print(f"Correo enviado a {email}")
        return f"Correo enviado a {email}"
    except Exception as e:
        self.retry(exc=e, countdown=10, max_retries=3)


@shared_task(bind=True)
def enviar_whatsapp(self, cel):
    try:
        print(f"Enviando whatsapp {cel}")
        time.sleep(5)
        print("Whatsapp enviado correctamente")
        return f"whatsApp enviado {cel}"
    except Exception as e:
        self.retry(exc=e, countdown=10, max_retries=3)

# para probar desde la terminal
"""
from core.tasks import enviar_correo, enviar_whatsapp

emails = ["email1@gmail.com","email2@gmail.com","email3@gmail.com","email4@gmail.com"]
celus = ["1623014898","1174562596","1522589632","1120258596"]

for email in emails:
  enviar_correo.delay(email)

for cel in celus:
  enviar_whatsapp.delay(cel)

"""


# ejemplo individual
"""
resultado = enviar_correo.delay("test@example.com")
print(resultado.status)
"""