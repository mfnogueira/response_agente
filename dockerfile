# Use uma imagem base oficial do Python
FROM python:3.12-slim

# Configurações do Poetry
ENV POETRY_VERSION=1.3.2
RUN pip install poetry==$POETRY_VERSION

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie o pyproject.toml e o poetry.lock para o diretório de trabalho
COPY pyproject.toml poetry.lock /app/

# Instale as dependências do Poetry
RUN poetry config virtualenvs.create false \
    && poetry install --no-root --only main

# Copie todo o projeto para o diretório de trabalho
COPY . /app

# Exponha a porta usada pelo Streamlit
EXPOSE 8501

# Comando para rodar o Streamlit
CMD ["streamlit", "run", "streamlit_app.py"]
