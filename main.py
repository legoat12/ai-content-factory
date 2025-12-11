import time
import requests
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def generate_script(topic):
    prompt = f"Ecris un court script viral TikTok dans le thème : {topic}."
    r = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers={"Authorization": f"Bearer {OPENAI_API_KEY}"},
        json={
            "model": "gpt-4o-mini",
            "messages": [{"role": "user", "content": prompt}]
        }
    )

    # Sécurise en cas d'erreur API
    try:
        return r.json()["choices"][0]["message"]["content"]
    except:
        return "Erreur API"

def main_loop():
    topics = [
        "gaming", "motivation", "avion", "robot",
        "histoire qui fait peur", "video drôle", "foot"
    ]

    print("\n🚀 AI Content Factory démarrée...\n")

    while True:
        for t in topics:
            script = generate_script(t)
            print(f"\n[✔] Script généré ({t}) :\n{script}\n")
            time.sleep(5)

        print("\n--- Nouvelle boucle dans 2 minutes ---\n")
        time.sleep(120)

if __name__ == "__main__":
    main_loop()
