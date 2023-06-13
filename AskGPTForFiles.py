import configparser
import os
from langchain import PromptTemplate
from langchain.llms import OpenAI
from langchain import HuggingFaceHub

# Params
user_name = 'Alejandro'
directory_path = './Data'  # Ruta de la carpeta a analizar
langchain_model = 'OpenAI' 
prompt_custom_template = 'EducationalAssistant'

open_ai_model_temperature = 0.9
open_ai_model_name = "gpt-3.5-turbo-0301"

# Read config
config = configparser.ConfigParser()
config.read('config.ini')

# Extraer información de los archivos y carpetas
def process_directories(path):
    tema_principal = ''
    temas_objetivo = []
    texto = ''
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".txt"):
                tema_principal = os.path.basename(root)
                with open(os.path.join(root, file), 'r', errors='ignore') as file_obj:
                    texto = file_obj.read()
        for dir in dirs:
            temas_objetivo.append(dir)
    return tema_principal, temas_objetivo, texto

# Choose the prompt
def create_prompt(template_type, texto, tema_principal, tema_objetivo):
    if template_type == 'EducationalAssistant':
        template = config['prompts']['EducationalAssistant']
        return PromptTemplate(template=template, input_variables=['contenido', 'tema_principal', 'tema_objetivo']).format(contenido=texto, tema_principal=tema_principal, tema_objetivo=tema_objetivo)

# Ask the LLM
def ask_llm(model, text):
    if model == 'OpenAI':
        os.environ['OPENAI_API_KEY'] = config['api_key']['openai']
        return OpenAI(temperature=open_ai_model_temperature, model_name=open_ai_model_name)(text)

# Guarda el texto generado en la carpeta correspondiente
def save_text_to_folder(text, folder_path):
    with open(os.path.join(folder_path, "generated_text.txt"), 'w') as file_obj:
        file_obj.write(text)

# Main
tema_principal, temas_objetivo, texto = process_directories(directory_path)
for tema_objetivo in temas_objetivo:
    prompt = create_prompt(prompt_custom_template, texto, tema_principal, tema_objetivo)
    print(prompt)
    generated_text = ask_llm(langchain_model, prompt)
    print(generated_text)
    save_text_to_folder(generated_text, os.path.join(directory_path, tema_objetivo))
