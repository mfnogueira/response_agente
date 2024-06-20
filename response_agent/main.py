import os
from dotenv import load_dotenv
from response_agent.gerente import Gerente
from response_agent.vetorizar import vetorizar

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

# Obter a chave API do Llama2
llama2_api_key = os.getenv("LLAMA2_API_KEY")

# Inicializar o gerente
gerente = Gerente(llama2_api_key)

def main():
    # Vetorizar arquivos de exemplo
    vetorizar("path/to/your/file.csv", "futebol")
    vetorizar("path/to/your/file.pdf", "formula1")

    # Exemplo de uso
    pergunta_futebol = "Quem ganhou o último Campeonato Brasileiro?"
    resposta_futebol = gerente.encaminhar_pergunta("futebol", pergunta_futebol)
    print(f"Resposta sobre Futebol: {resposta_futebol}")

    pergunta_formula1 = "Quem ganhou o último Grande Prêmio de Mônaco?"
    resposta_formula1 = gerente.encaminhar_pergunta("formula1", pergunta_formula1)
    print(f"Resposta sobre Fórmula 1: {resposta_formula1}")

if __name__ == "__main__":
    main()
