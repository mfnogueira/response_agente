import streamlit as st
from response_agent.gerente import Gerente
from dotenv import load_dotenv
import os

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

# Obter a chave API do Llama2
llama2_api_key = os.getenv("LLAMA2_API_KEY")

# Inicializar o gerente
gerente = Gerente(llama2_api_key)

# Configuração da página do Streamlit
st.set_page_config(page_title="Sports Q&A", page_icon=":soccer:", layout="wide")

# Título do app
st.title("Sports Q&A with AI")

# Seleção do tipo de esporte
specialty = st.selectbox(
    "Selecione o esporte",
    ["futebol", "volei", "basquete", "ufc", "formula1"]
)

# Campo de input para a pergunta
question = st.text_input("Faça sua pergunta:")

# Botão para enviar a pergunta
if st.button("Perguntar"):
    if question:
        # Encaminhar a pergunta para o gerente
        response = gerente.encaminhar_pergunta(specialty, question)
        
        # Exibir a resposta
        st.subheader("Resposta:")
        st.write(response)
        
        # Simulação de dados para gráficos (substitua com dados reais)
        data = {
            "Categoria": ["Categoria 1", "Categoria 2", "Categoria 3"],
            "Valores": [10, 20, 30]
        }
        
        # Gráfico de barras
        st.bar_chart(data)
        
        # Gráfico de linhas
        st.line_chart(data)
    else:
        st.error("Por favor, insira uma pergunta.")

# Rodapé
st.markdown("Desenvolvido com 💻 por [Seu Nome](https://github.com/seu-usuario)")
