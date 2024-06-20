from langchain.llms import Llama2
from vector_stores import vector_stores

PROMPTS = {
    "futebol": "Você é um especialista em futebol. Responda à seguinte pergunta: {question}",
    "volei": "Você é um especialista em vôlei. Responda à seguinte pergunta: {question}",
    "basquete": "Você é um especialista em basquete. Responda à seguinte pergunta: {question}",
    "ufc": "Você é um especialista em UFC. Responda à seguinte pergunta: {question}",
    "formula1": "Você é um especialista em Fórmula 1. Responda à seguinte pergunta: {question}"
}

def agente_especialista(specialty, question, api_key):
    llama2_model = Llama2(api_key=api_key)
    prompt = PROMPTS[specialty].format(question=question)
    relevant_info = vector_stores[specialty].search(question)
    combined_prompt = f"{prompt}\nInformações relevantes: {relevant_info}"
    response = llama2_model.generate(combined_prompt)
    return response
