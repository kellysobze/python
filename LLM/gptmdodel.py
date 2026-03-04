from LLMmodel import LLMODEL

class Gptmdodel(LLMODEL):
    def genera(self,prompt):
        return f'Risposta locale per {prompt}'

