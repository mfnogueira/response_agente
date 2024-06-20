from agentes import agente_especialista

class Gerente:
    def __init__(self, api_key):
        self.api_key = api_key
        self.agents = {
            "futebol": agente_especialista,
            "volei": agente_especialista,
            "basquete": agente_especialista,
            "ufc": agente_especialista,
            "formula1": agente_especialista
        }

    def encaminhar_pergunta(self, specialty, question):
        if specialty in self.agents:
            return self.agents[specialty](specialty, question, self.api_key)
        else:
            return "Desculpe, não tenho um agente para essa especialidade."
