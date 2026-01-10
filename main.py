from openai import OpenAI
from dotenv import load_dotenv
import os


def main() -> None:
    load_dotenv()

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    messages = [
        {"role": "system", "content": "Eres un chatbot amable y útil."}
    ]

    print("🤖 Chatbot iniciado (escribe 'salir' para terminar)\n")

    while True:
        user_input = input("Tú: ")
        if user_input.lower() == "salir":
            print("👋 Hasta luego")
            break

        messages.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )

        reply = response.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        print("Pensando...")
        print(f"Bot: {reply}\n")



if __name__ == "__main__":
    main()
