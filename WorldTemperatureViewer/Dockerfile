# Usar una imagen base de Python
FROM python:3.10.10-slim-buster

# Establecer un directorio de trabajo
WORKDIR /app

# Copiar los archivos de requisitos e instalar las dependencias
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Copiar el resto de los archivos de la aplicación
COPY . .

# Exponer el puerto para Streamlit
EXPOSE 8501

# Comando para ejecutar la aplicación
CMD ["streamlit", "run", "WTB.py"]
