Entro al [marketplace de github](https://github.com/marketplace)  → models → catalog

voy a seleccionar este para probar: [gpt-4o-mini](https://github.com/marketplace/models/azure-openai/gpt-4o-mini)

**Configurar token/Authenticacion**

1. Voy al settings de github
2. voy a developer settings
3. voy a personal access token
    1. click en tokens classic
    2. Generate new token
    3. personal access token (classic)
    4. Solo tengo que chequear read:packages    
4. click boton verde generate new token
5. Copiar el token en algún lugar seguro

**Instalar las dependencias**

En mi caso estoy usando python así que el comando para instalar las dependencias en mi entorno virtual (python -m venv env)

```bash
activo entorno virtual:  .\env\Scripts\activate 
pip install openai
ejecuto proyecto:  python .\main.py  
```