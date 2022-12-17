FROM python:3.8

# Cria um diretório para o código do projeto
RUN mkdir /code

# Define /code como o diretório de trabalho
WORKDIR /code

# Copia os arquivos do projeto para o diretório de trabalho
COPY . /code/

RUN pip install django

# Expõe a porta 8000 para o mundo externo
EXPOSE 8000

# Define o comando padrão para iniciar o servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]