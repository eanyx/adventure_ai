import openai

# Configuration de la clé API
client = openai.OpenAI(api_key="VOTRE_CLE_API")

def generer_reponse(prompt, historique):
    # On ajoute le message du joueur à l'historique
    messages = [{"role": "system", "content": "Tu es le maître d'un jeu d'aventure médiéval-fantastique. Sois descriptif mais concis."}]
    messages.extend(historique)
    messages.append({"role": "user", "content": prompt})

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    
    return response.choices[0].message.content

def jeu():
    print("--- BIENVENUE DANS L'AVENTURE IA ---")
    historique = []
    
    # Introduction
    intro = "Tu te réveilles au bord d'une forêt sombre. Que fais-tu ?"
    print(f"\nIA: {intro}")
    
    while True:
        action = input("\nVous: ")
        
        if action.lower() in ["quitter", "exit", "stop"]:
            print("Merci d'avoir joué !")
            break
            
        # Obtenir la suite de l'histoire
        reponse_ia = generer_reponse(action, historique)
        
        # Mise à jour de l'historique pour la mémoire du jeu
        historique.append({"role": "user", "content": action})
        historique.append({"role": "assistant", "content": reponse_ia})
        
        print(f"\nIA: {reponse_ia}")

if __name__ == "__main__":
    jeu()