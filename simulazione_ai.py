import json



with open("utenti.json",'r') as f:
    u=json.load(f)
def vincenzo_gpt(prompt,context):
    risposta="ciao,ecco la tua descrizione:\n"
    descrizione = f"L'utente si chiama {context['nome']} e ha {context:['eta']}anni"
    return risposta +descrizione