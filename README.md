# AskGPTForFiles
Este proyecto utiliza la API de OpenAI para generar textos en carpetas específicas basándose en el contenido de un archivo de texto de una carpeta dada. Específicamente, buscará en la carpeta dada y sus subcarpetas cualquier archivo de texto. Tomará el nombre de la carpeta del contenido como "TemaPrincipal" y los nombres de las otras carpetas como "TemasObjetivo". Luego creará un prompt personalizado y generará textos para las carpetas de los "TemasObjetivo", utilizando la misma estructura que el contenido del archivo original.

## Instalación
Para instalar las dependencias necesarias para este proyecto, por favor, ejecuta el siguiente comando en tu terminal:

´´´
pip install -r requirements.txt
´´´

## Uso
Para utilizar este script, necesitas tener una clave de API de OpenAI.

Configura tu clave de API en el archivo config.ini bajo el apartado [api_key].

´´´
[api_key]
openai = YOUR_OPENAI_API_KEY
´´´

Define el directorio que quieres procesar en la variable directory_path.

Ejecuta el script de Python en tu terminal:
´´´
python AskGPTForFiles.py
´´´

El script buscará en el directorio dado y sus subdirectorios cualquier archivo de texto. Tomará el nombre de la carpeta que contiene el archivo como "TemaPrincipal" y los nombres de las otras carpetas como "TemasObjetivo". Luego generará un texto para cada "TemaObjetivo", utilizando el contenido del archivo original como plantilla, y guardará el texto generado en la carpeta correspondiente.

## Dependencias
Este proyecto utiliza las siguientes bibliotecas:

- configparser
- os
- LangChain
- OpenAI

Puedes instalar todas las dependencias necesarias con el comando pip install -r requirements.txt.